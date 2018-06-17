def process_group_entities(group, grouped_entities, hass, logger, process_group_entities, processed_groups):
#  logger.warn("processing group {}, currently {} grouped items".format(group.entity_id, len(grouped_entities)))

  processed_groups.append(group.entity_id)
  for e in group.attributes["entity_id"]:
    domain = e.split(".")[0]
    if domain == "group":
      g = hass.states.get(e)
      if (g is not None) and (g.entity_id not in processed_groups):
        process_group_entities(g, grouped_entities, hass, logger, process_group_entities, processed_groups)
#  logger.warn("finishing group {}, currently {} grouped items".format(group.entity_id, len(grouped_entities)))

def scan_for_dead_entities(hass, logger, data, process_group_entities):
  target_group=data.get("target_group","deaditems")

  real_entities = set()
  grouped_entities = set()
  processed_groups=[]

  for s in hass.states.all():
    domain = s.entity_id.split(".")[0]
    if domain != "group":
      real_entities.add(s.entity_id)
    else:
      if (("view" not in s.attributes) or
          ( s.attributes["view"] == False)):
        real_entities.add(s.entity_id)
      process_group_entities(s, grouped_entities, hass, logger, process_group_entities, processed_groups)

  entity_ids=[]
  counter=0
  for e in (grouped_entities - real_entities):
    name = "weblink.deaditem{}".format(counter)
    hass.states.set(name, "javascript:return false", {"friendly_name":e})
    entity_ids.append(name)
    counter = counter +1

  service_data = {'object_id': target_group, 'name': 'Nonexisting Items',
                    'view': False, 'control': 'hidden',
                    'entities': entity_ids, 'visible': True}

  hass.services.call('group', 'set', service_data, False)

scan_for_dead_entities(hass, logger, data, process_group_entities)

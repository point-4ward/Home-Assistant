def scan_for_new_entities(hass, logger, data):
    ignore = data.get("domains_to_ignore", "zone,automation,script")
    domains_to_ignore = ignore.replace(" ", "").split(",")
    target_group = data.get("target_group", "group.catchall")
    show_if_empty = data.get("show_if_empty", False)
    min_items_to_show = data.get("min_items_to_show", 1)

    entity_ids = []
    groups = []

    for s in hass.states.all():
        state = hass.states.get(s.entity_id)
        domain = state.entity_id.split(".")[0]

        if (domain not in domains_to_ignore):
            if (domain != "group"):
                if (("hidden" not in state.attributes) or
                        (state.attributes["hidden"] == False)):
                    entity_ids.append(state.entity_id)
            else:
                if (("view" not in state.attributes) or
                        (state.attributes["view"] == False)):
                    entity_ids.append(state.entity_id)

        if (domain == "group") and (state.entity_id != target_group):
            groups.append(state.entity_id)

    for groupname in groups:
        group = hass.states.get(groupname)
        for a in group.attributes["entity_id"]:
            if a in entity_ids:
                entity_ids.remove(a)

    if (len(entity_ids)) > min_items_to_show or show_if_empty:
        visible = True
    else:
        visible = False

    service_data = {'object_id': 'catchall', 'name': 'Ungrouped Items',
                    'view': False, 'visible': visible,
                    'control': 'hidden', 'entities': entity_ids}

    hass.services.call('group', 'set', service_data, False)

scan_for_new_entities(hass, logger, data)

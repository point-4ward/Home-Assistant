on = 0
for entity_id in hass.states.entity_ids('automation'):
    state = hass.states.get(entity_id)
    if state.state == 'on':
        on = on + 1

hass.states.set('sensor.automation_on', on, {'unit_of_measurement': 'on'})
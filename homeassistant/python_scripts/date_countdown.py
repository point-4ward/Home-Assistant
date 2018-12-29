""" This script creates a sensor that a counts down to the next occurrance """
"""   of a date, like a birthday or anniversary and gives the number of    """
"""                         years as an attribute                          """


"""       Requires python_script: to be enabled in you configuration       """


""" Usage:                                                                 """
"""                                                                        """
""" automation:                                                            """
"""   alias: Refresh John's birthday sensor                                """
"""   trigger:                                                             """
"""     platform: time                                                     """
"""     at: '00:00:01'                                                     """
"""   action:                                                              """
"""     service: python_script.date_countdown                              """
"""     data:                                                              """
"""       name: John                                                       """
"""       type: birthday                                                   """
"""       date: 17/08/1971   #DD/MM/YYYY                                   """


"""  This will create a sensor with entity_id sensor.birthday_john and a   """
"""  friendly name of 'John's birthday' .  The sensors value will be the   """
"""   number of days until the birthday, and the attribute 'years' will    """
"""          show how old John will be on his next birthday                """



today = datetime.datetime.now().date()

name = data.get('name')
type = data.get('type')
sensorName = "sensor.{}_{}".format(type , name.replace(" " , "_"))

dateStr = data.get('date')
dateSplit = dateStr.split("/")

dateDay = int(dateSplit[0])
dateMonth = int(dateSplit[1])
dateYear =  int(dateSplit[2])
date = datetime.date(dateYear,dateMonth,dateDay)

thisYear = today.year
nextOccur = datetime.date(thisYear , dateMonth , dateDay)

numberOfDays = 0
years = int(thisYear) - dateYear


if today < nextOccur:
  nextOccur = datetime.date(thisYear+1 , dateMonth , dateDay)
  numberOfDays = (nextOccur - today).days

elif today > nextOccur:
  nextOccur = datetime.date(thisYear+1 , dateMonth , dateDay)
  numberOfDays = int((nextOccur - today).days)
  years = years+1


hass.states.set(sensorName , numberOfDays ,
  {
    "icon" : "mdi:calendar-star" ,
    "unit_of_measurement" : "days" ,
    "friendly_name" : "{}'s {}".format(name, type) ,
    "years" : years
  }
)

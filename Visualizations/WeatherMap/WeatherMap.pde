JSONArray values;

void setup()
{
  values = loadJSONArray("WeatherMapTestObject.txt");
  
  for (int i = 0; i < values.size(); i++) 
  {
     JSONObject operator = values.getJSONObject(i); 

     int lastheard = operator.getInt("lastheard");
     String callsign = operator.getString("callsign");
     String ssid = operator.getString("ssid");
     
     println(callsign + "-" + ssid + " was last heard at " + lastheard);
  }

}
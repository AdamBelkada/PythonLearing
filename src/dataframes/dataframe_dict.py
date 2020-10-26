import pandas as pd

# def default_timeline_get():

default_timeline_source = [
        (110, pd.to_datetime("2020-09-02 16:03:25") ,pd.to_datetime("2020-09-02 18:29:03"), 1,  "Turbine OK"            , 100)
      , (110, pd.to_datetime("2020-09-02 18:29:04"), pd.to_datetime("2020-09-04 10:45:24"), 7,  "Gearbox Vibration"     , 100)
      , (110, pd.to_datetime("2020-09-04 10:45:25"), pd.to_datetime("2020-09-07 08:14:56"), 9,  "Gearbox Disconnected"  , 100)
      , (110, pd.to_datetime("2020-09-07 08:14:57"), pd.to_datetime("2020-09-12 15:27:18"), 1,  "Turbine OK"            , 100)
      , (110, pd.to_datetime("2020-09-12 15:27:19"), pd.to_datetime("2020-09-12 21:16:37"), 15, "Low RPM"               , 100)
      , (98,  pd.to_datetime("2020-09-02 15:27:19"), pd.to_datetime("2020-09-10 04:39:20"), 1,  "Turbine OK"            , 100)
      , (98,  pd.to_datetime("2020-09-10 04:39:21"), pd.to_datetime("2020-09-12 14:25:11"), 7,  "Blade Pitch Too Steep" , 100)
    ]

default_timeline_source_labels = [
        "asset_key"
      , "event_start"
      , "event_end"
      , "iec_category"
      , "event_code"
      , "gads_id"
    ]

default_timeline = pd.DataFrame.from_records( default_timeline_source, columns=default_timeline_source_labels )
default_timeline = default_timeline.convert_dtypes()

    # return default_timeline
print (default_timeline["event_code"][1])
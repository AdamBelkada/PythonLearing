import pandas as pd
import numpy as np
# set the display option to maximum to have a good view of the data
pd.set_option("display.expand_frame_repr", None, "display.max_columns", None)
# pd.set_option('display.max_columns', None)
default_allocations_df = pd.DataFrame({
            "asset_key"                  : "PROJ1_TUR1"
            ,"event_start"               : ["2020-09-03 00:00:00","2020-09-05 00:00:00"]
            ,"event_end"                 : ["2020-09-05 00:00:00","2020-09-08 00:00:00"]
            ,"iec_category"              : ["6","60"]
            ,"event_code"                : [10,100]
            ,"gads_id"                   : [9,90]
        })

manual_reclassifications_df = pd.DataFrame(
       {
            "asset_key"                  : "PROJ1_TUR1"
            ,"event_start"               : ["2020-09-04 00:00:00","2020-09-06 00:00:00"]
            ,"event_end"                 : ["2020-09-06 00:00:00","2020-09-07 00:00:00"]
            ,"iec_category"              : ["6","60"]
            ,"iec_category_reclassified" : ["8","80"]
            ,"event_code"                : [10,10]
            ,"event_code_reclassified"   : [7,14]
            ,"gads_id"                   : [9,90]
            ,"gads_id_reclassified"      : [100,200]
            ,"event_reclassification_id" : [777,555]
        }
        )

# get all the different dates
# TODO: Creation of event_boundaries is a good candidate for a sub-function.
distinct_dates = default_allocations_df["event_start"]
distinct_dates = distinct_dates.append(default_allocations_df["event_end"])

# get manual reclassifications if not None
if manual_reclassifications_df is not None:
        distinct_dates = distinct_dates.append(manual_reclassifications_df["event_start"])
        distinct_dates = distinct_dates.append(manual_reclassifications_df["event_end"])

distinct_dates.drop_duplicates(keep = "first", inplace = True)
distinct_dates.sort_values(ascending = True, kind = "mergesort", ignore_index = True, inplace = True)

# get pairs of dates out of distincts_dates
date_boundaries_df = pd.DataFrame(distinct_dates,columns=['event_start'])
print (date_boundaries_df)
date_boundaries_df['event_end']=pd.DataFrame(date_boundaries_df['event_start'].shift(-1))

# remove the last record with Na end date
date_boundaries_df =date_boundaries_df.dropna()
print (date_boundaries_df)

# define a dataframe that will hold the cet results
cet_results = pd.DataFrame(
        {
            "asset_key"                  : pd.Series([], dtype="string")
            ,"event_start"               : pd.Series([], dtype="datetime64[ns]")
            ,"event_end"                 : pd.Series([], dtype="datetime64[ns]")
            ,"iec_category"              : pd.Series([], dtype="string")
            ,"event_code"                : pd.Series([], dtype="int32")
            ,"gads_id"                   : pd.Series([], dtype="int32")
            ,"iec_category_reclassified" : pd.Series([], dtype="string")         
            ,"event_code_reclassified"   : pd.Series([], dtype="int32")            
            ,"gads_id_reclassified"      : pd.Series([], dtype="int32") 
            ,"event_reclassification_id" : pd.Series([], dtype="Int64") 
        }
    )

#loop through the dates paire boundaries 
print ("looping through the date boundaries")
for index,event_boundary in date_boundaries_df.iterrows():
    event_start = event_boundary["event_start"]
    event_end   = event_boundary["event_end"]
    print ("event between these dates",event_start," & ",event_end)                                                                                                                                                                                                                                                                                                 

    # define the default allocation
    default_event = (default_allocations_df[( default_allocations_df["event_start"]<event_end)
                                    & 
                                  (default_allocations_df["event_end"]>event_start )   
                                 ]).reset_index(drop=True) 
    
    print ("default: \n",default_event)
    cet_current_new = pd.DataFrame(
        {
            "asset_key"                  :default_event["asset_key"    ][0]           
            ,"event_start"               :event_start
            ,"event_end"                 :event_end
            ,"iec_category"              :default_event["iec_category" ][0]
            ,"iec_category_reclassified" :default_event["iec_category" ][0]
            ,"event_code"                :default_event["event_code"   ][0]
            ,"event_code_reclassified"   :default_event["event_code"   ][0]
            ,"gads_id"                   :default_event["gads_id"      ][0]
            ,"gads_id_reclassified"      :default_event["gads_id"      ][0]
            ,"event_reclassification_id" :np.nan
        },index=[0]
    )   
    # define the manual reclassification if exist

    manual_event=(manual_reclassifications_df[( manual_reclassifications_df["event_start"]<event_end)
                                    & 
                                  (manual_reclassifications_df["event_end"]>event_start )   
                                 ]).reset_index(drop=True) 
    print(manual_event)
    # manual_event=manual_event.reset_index(drop=True)                      
                             
    if not manual_event.empty :
        print("manual reclassification: \n",manual_event)
        cet_current_new["iec_category_reclassified"]=manual_event["iec_category_reclassified"]
        cet_current_new["event_code_reclassified"  ]=manual_event["event_code_reclassified"  ]
        cet_current_new["gads_id_reclassified"     ]=manual_event["gads_id_reclassified"     ]
        cet_current_new["event_reclassification_id"]=manual_event["event_reclassification_id"]
        
    else:
        print("no manual")
    
    print ("new cet entry: \n",cet_current_new)
    cet_results = cet_results.append(cet_current_new)

print ("final result\n",cet_results)
print (cet_results.dtypes)
        
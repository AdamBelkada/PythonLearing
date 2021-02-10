from approvaltests.approvals import verify
import pandas as pd

def test_simple():
    # result = "Hello ApprovalTests"
    result = pd.DataFrame(
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
                ,"event_reclassification_id" : pd.Series([], dtype="int32") 
            }
        )
    structure = result.dtypes
    print (structure)
    verify(structure.to_string())


def main():
    test_simple()
if __name__ =='__main__':
    main()
    #C:\Program Files (x86)\Meld
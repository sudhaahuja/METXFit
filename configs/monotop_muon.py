


out_file_name = 'monotop_muon_temp.root'

bins = [160.0,180.0,200.0,220.0,240.0,1000.0]

# will expect samples with sample_sys_Up/Down but will skip if not found 
systematics=["btag","mistag"]

#samples = {}

#lepmonotop_category = {}

lepmonotop_category = {
        'name':"lepmonotop"
        #,'in_file_name':"/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_v2/flat/limits/fittingForest_monojet_"+s+".root"
        ,'in_file_name':" file "
        ,"cutstring":""
        ,"varstring":["min(999.9999,mT)",160,1000]
        ,"weightname":"weight"
        ,"bins":bins[:]
        ,"additionalvars":[]
        ,"pdfmodel":0
	,"samples":
             {  
		  # Signal Region
		  #"Zvv_signale"    	       :['signal','zjets',1,0]
                  "Zll_signalm"	               :['signal','zll',1,0]
 		  ,"Wlv_signalm"  	       :['signal','wjets',1,0]
		  ,"Diboson_signalm"  	       :['signal','dibosons',1,0]
		  ,"ttbar_signalm"   	       :['signal','ttbar',1,0]
		  ,"ST_signalm"                :['signal','stop',1,0]
		  ,"QCD_signalm"	       :['signal','qcd',1,0]
		  ,"Data_signalm"	       :['signal','data',0,0]
		  # signals
                  #,"hsDM_1000_50_100_signal"    :['signal','hsDM-1000-50-100_signal',1,1]

                   # Single muon (w) control
                  ,"Zll_wmn"     	       :['singlemuonw','zll',1,0]
 		  ,"Wlv_wmn"      	       :['singlemuonw','wjets',1,0]
		  ,"Diboson_wmn"               :['singlemuonw','dibosons',1,0]
		  ,"ttbar_wmn"                 :['singlemuonw','ttbar',1,0]
		  ,"ST_wmn"                    :['singlemuonw','stop',1,0]
		  ,"QCD_wmn"	               :['singlemuonw','qcd',1,0]
		  ,"Data_wmn"	               :['singlemuonw','data',0,0]

		  # Single muon (top) control
                  ,"Zll_ttbar1m"                :['ttbarmuon','zll',1,0]
                  ,"Wlv_ttbar1m"               :['ttbarmuon','wjets',1,0]
		  ,"Diboson_ttbar1m"           :['ttbarmuon','dibosons',1,0]
		  ,"ttbar_ttbar1m"             :['ttbarmuon','ttbar',1,0]
		  ,"ST_ttbar1m"                :['ttbarmuon','stop',1,0]
		  ,"QCD_ttbar1m"               :['ttbarmuon','qcd',1,0]
		  ,"Data_ttbar1m"              :['ttbarmuon','data',0,0]

                   # two leptons (ttbar)m control
                  ,"Zll_ttbar2lm"               :['ttbar2mleptons','zll',1,0]
                  ,"Wlv_ttbar2lm"              :['ttbar2mleptons','wjets',1,0]
                  ,"Diboson_ttbar2lm"          :['ttbar2mleptons','dibosons',1,0]
                  ,"ttbar_ttbar2lm"            :['ttbar2mleptons','ttbar',1,0]
                  ,"ST_ttbar2lm"               :['ttbar2mleptons','stop',1,0]
                  ,"QCD_ttbar2lm"              :['ttbar2mleptons','qcd',1,0]
                  ,"Data_ttbar2lm"             :['ttbar2mleptons','data',0,0]

                  }

}
categories = [lepmonotop_category]

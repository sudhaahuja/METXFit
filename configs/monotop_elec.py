


out_file_name = 'monotop_elec_temp.root'

bins = [160.0,180.0,200.0,220.0,240.0,1000.0]

# will expect samples with sample_sys_Up/Down but will skip if not found 
systematics=["btag","mistag"]

#samples = {}

#lepmonotop_category = {}

lepmonotop_category = {
        'name':"lepmonotop"
        #,'in_file_name':"/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_v2/flat/limits/fittingForest_monojet_"+s+".root"
        ,'in_file_name':"/uscms/home/dsilveri/nobackup/PandaAnalysis_2018/CMSSW_8_0_29/src/PandaAnalysis/LeptonicMonoTop/fitting/fittingForest_lepmonotop.root"
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
                  "Zll_signale"	               :['signal','zll',1,0]
 		  ,"Wlv_signale"  	       :['signal','wjets',1,0]
		  ,"Diboson_signale"  	       :['signal','dibosons',1,0]
		  ,"ttbar_signale"   	       :['signal','ttbar',1,0]
		  ,"ST_signale"                :['signal','stop',1,0]
		  ,"QCD_signale"	       :['signal','qcd',1,0]
		  ,"Data_signale"	       :['signal','data',0,0]
		  # signals
                  #,"hsDM_1000_50_100_signal"    :['signal','hsDM-1000-50-100_signal',1,1]

		  # Single electron (top) control
                  ,"Zll_ttbar1e"       	       :['ttbarelectron','zll',1,0]
 		  ,"Wlv_ttbar1e"               :['ttbarelectron','wjets',1,0]
		  ,"Diboson_ttbar1e"           :['ttbarelectron','dibosons',1,0]
		  ,"ttbar_ttbar1e"             :['ttbarelectron','ttbar',1,1]
		  ,"ST_ttbar1e"                :['ttbarelectron','stop',1,0]
		  ,"QCD_ttbar1e"               :['ttbarelectron','qcd',1,0]
		  ,"Data_ttbar1e"     	       :['ttbarelectron','data',0,0]

                   # Single electron (w) control
                  ,"Zll_wen"                   :['singleelectronw','zll',1,0]
 		  ,"Wlv_wen"                   :['singleelectronw','wjets',1,0]
		  ,"Diboson_wen"               :['singleelectronw','dibosons',1,0]
		  ,"ttbar_wen"                 :['singleelectronw','ttbar',1,0]
		  ,"ST_wen"                    :['singleelectronw','stop',1,0]
		  ,"QCD_wen"                   :['singleelectronw','qcd',1,0]
		  ,"Data_wen"                  :['singleelectronw','data',0,0]

                   # two leptons (ttbar)e control
                  ,"Zll_ttbar2le"              :['ttbar2eleptons','zll',1,0]
                  ,"Wlv_ttbar2le"              :['ttbar2eleptons','wjets',1,0]
                  ,"Diboson_ttbar2le"          :['ttbar2eleptons','dibosons',1,0]
                  ,"ttbar_ttbar2le"            :['ttbar2eleptons','ttbar',1,0]
                  ,"ST_ttbar2le"               :['ttbar2eleptons','stop',1,0]
                  ,"QCD_ttbar2le"              :['ttbar2eleptons','qcd',1,0]
                  ,"Data_ttbar2le"             :['ttbar2eleptons','data',0,0]


  }

}
categories = [lepmonotop_category]

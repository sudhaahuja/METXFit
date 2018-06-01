out_file_name = 'lepmonotop.root'
bins = [160.0,180.0,200.0,220.0,240.0,1000.0]
systematics=["btag","mistag"]

lepmonotop_muon_category = {
        'name':"lepmonotop_muon"
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
		  ,"ttbarlj_signalm"   	       :['signal','ttbarlj',1,0]
		  ,"ttbardil_signalm"  	       :['signal','ttbardil',1,0]
		  ,"ST_signalm"                :['signal','stop',1,0]
		  ,"QCD_signalm"	       :['signal','qcd',1,0]
		  ,"Data_signalm"	       :['signal','data',0,0]
		  # signals
                  #,"hsDM_1000_50_100_signal"    :['signal','hsDM-1000-50-100_signal',1,1]

                   # Single muon (w) control
                  ,"Zll_wmn"     	       :['singlemuonw','zll',1,0]
 		  ,"Wlv_wmn"      	       :['singlemuonw','wjets',1,0]
		  ,"Diboson_wmn"               :['singlemuonw','dibosons',1,0]
		  ,"ttbarlj_wmn"               :['singlemuonw','ttbarlj',1,0]
                  ,"ttbardil_wmn"              :['singlemuonw','ttbardil',1,0]
		  ,"ST_wmn"                    :['singlemuonw','stop',1,0]
		  ,"QCD_wmn"	               :['singlemuonw','qcd',1,0]
		  ,"Data_wmn"	               :['singlemuonw','data',0,0]

		  # Single muon (top) control
                  ,"Zll_tmn"                :['singlemuontop','zll',1,0]
                  ,"Wlv_tmn"               :['singlemuontop','wjets',1,0]
		  ,"Diboson_tmn"           :['singlemuontop','dibosons',1,0]
		  ,"ttbarlj_tmn"             :['singlemuontop','ttbarlj',1,0]
                  ,"ttbardil_tmn"             :['singlemuontop','ttbardil',1,0]
		  ,"ST_tmn"                :['singlemuontop','stop',1,0]
		  ,"QCD_tmn"               :['singlemuontop','qcd',1,0]
		  ,"Data_tmn"              :['singlemuontop','data',0,0]

                   # two leptons (ttbar)m control
                  ,"Zll_tme"               :['muonelectron','zll',1,0]
                  ,"Wlv_tme"              :['muonelectron','wjets',1,0]
                  ,"Diboson_tme"          :['muonelectron','dibosons',1,0]
                  ,"ttbarlj_tme"            :['muonelectron','ttbarlj',1,0]
                  ,"ttbardil_tme"            :['muonelectron','ttbardil',1,0]
                  ,"ST_tme"               :['muonelectron','stop',1,0]
                  ,"QCD_tme"              :['muonelectron','qcd',1,0]
                  ,"Data_tme"             :['muonelectron','data',0,0]

                  }

}
lepmonotop_electron_category = {
        'name':"lepmonotop_electron"
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
                  "Zll_signale"	               :['signal','zll',1,0]
 		  ,"Wlv_signale"  	       :['signal','wjets',1,0]
		  ,"Diboson_signale"  	       :['signal','dibosons',1,0]
		  ,"ttbarlj_signale"   	       :['signal','ttbarlj',1,0]
                  ,"ttbardil_signale"           :['signal','ttbardil',1,0]
		  ,"ST_signale"                :['signal','stop',1,0]
		  ,"QCD_signale"	       :['signal','qcd',1,0]
		  ,"Data_signale"	       :['signal','data',0,0]
		  # signals
                  #,"hsDM_1000_50_100_signal"    :['signal','hsDM-1000-50-100_signal',1,1]

                   # Single electron (w) control
                  ,"Zll_wen"     	       :['singleelectronw','zll',1,0]
 		  ,"Wlv_wen"      	       :['singleelectronw','wjets',1,0]
		  ,"Diboson_wen"               :['singleelectronw','dibosons',1,0]
		  ,"ttbarlj_wen"                 :['singleelectronw','ttbarlj',1,0]
                  ,"ttbardil_wen"                 :['singleelectronw','ttbardil',1,0]
		  ,"ST_wen"                    :['singleelectronw','stop',1,0]
		  ,"QCD_wen"	               :['singleelectronw','qcd',1,0]
		  ,"Data_wen"	               :['singleelectronw','data',0,0]

		  # Single electron (top) control
                  ,"Zll_ten"                :['singleelectrontop','zll',1,0]
                  ,"Wlv_ten"               :['singleelectrontop','wjets',1,0]
		  ,"Diboson_ten"           :['singleelectrontop','dibosons',1,0]
		  ,"ttbarlj_ten"             :['singleelectrontop','ttbarlj',1,0]
                  ,"ttbardil_ten"             :['singleelectrontop','ttbardil',1,0]
		  ,"ST_ten"                :['singleelectrontop','stop',1,0]
		  ,"QCD_ten"               :['singleelectrontop','qcd',1,0]
		  ,"Data_ten"              :['singleelectrontop','data',0,0]

                   # two leptons (ttbar)m control
                  ,"Zll_tem"               :['electronmuon','zll',1,0]
                  ,"Wlv_tem"              :['electronmuon','wjets',1,0]
                  ,"Diboson_tem"          :['electronmuon','dibosons',1,0]
                  ,"ttbarlj_tem"            :['electronmuon','ttbarlj',1,0]
                  ,"ttbardil_tem"            :['electronmuon','ttbardil',1,0]
                  ,"ST_tem"               :['electronmuon','stop',1,0]
                  ,"QCD_tem"              :['electronmuon','qcd',1,0]
                  ,"Data_tem"             :['electronmuon','data',0,0]

                  }

}
categories = [lepmonotop_muon_category,lepmonotop_electron_category]

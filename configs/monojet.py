


out_file_name = 'monojet_temp.root'

bins = [250.0, 280.0, 310.0, 340.0, 370.0, 400.0, 430.0, 470.0, 510.0, 550.0, 590.0, 640.0, 690.0, 740.0, 790.0, 840.0, 900.0, 960.0, 1020.0, 1090.0, 1160.0, 1250.0]

# will expect samples with sample_sys_Up/Down but will skip if not found 
systematics=["btag","mistag"]

#samples = {}

monojet_category = {}

for s in ['0tag','1tag', '2tag']:
     monojet_category[s] = {
        'name':"monojet_"+s
        #,'in_file_name':"/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_v2/flat/limits/fittingForest_monojet_"+s+".root"
        ,'in_file_name':"/uscms/home/naina25/nobackup/Panda_2018/Panda_Analysis/CMSSW_8_0_29/src/PandaAnalysis/SuperMonoJet/fitting/fittingForest_monojet_"+s+".root"
        ,"cutstring":""
        ,"varstring":["min(999.9999,met)",250,1000]
        ,"weightname":"weight"
        ,"bins":bins[:]
        ,"additionalvars":[]
        ,"pdfmodel":0
	,"samples":
             {  
		  # Signal Region
#		   "VH_signal"    	       :['signal','vh',1,0]
		  "Zvv_signal"    	       :['signal','zjets',1,0]
                  ,"Zll_signal"	               :['signal','zll',1,0]
 		  ,"Wlv_signal"  	       :['signal','wjets',1,0]
		  ,"Diboson_signal"  	       :['signal','dibosons',1,0]
		  ,"ttbar_signal"   	       :['signal','ttbar',1,0]
		  ,"ST_signal"                 :['signal','stop',1,0]
		  ,"QCD_signal"		       :['signal','qcd',1,0]
		  ,"Data_signal"	       :['signal','data',0,0]
		  # signals
                  ,"hsDM_1000_50_100_signal"    :['signal','hsDM-1000-50-100_signal',1,1]
                  ,"hsDM_1000_50_200_signal"    :['signal','hsDM-1000-50-200_signal',1,1]
                  ,"hsDM_1000_50_250_signal"    :['signal','hsDM-1000-50-250_signal',1,1]
                  ,"hsDM_1000_50_300_signal"    :['signal','hsDM-1000-50-300_signal',1,1]
                  
                  ,"ZpDM_1000_150_10_signal"    :['signal','ZpDM-1000-150-10_signal',1,1]
                  ,"ZpDM_1000_50_10_signal"    :['signal','ZpDM-1000-50-10_signal',1,1]
                  ,"ZpDM_100_150_10_signal"    :['signal','ZpDM-100-150-10_signal',1,1]
                  ,"ZpDM_100_50_10_signal"    :['signal','ZpDM-100-50-10_signal',1,1]
                  ,"ZpDM_1500_150_10_signal"    :['signal','ZpDM-1500-150-10_signal',1,1]
                  ,"ZpDM_1500_50_10_signal"    :['signal','ZpDM-1500-50-10_signal',1,1]
                  ,"ZpDM_2000_150_10_signal"    :['signal','ZpDM-2000-150-10_signal',1,1]
                  ,"ZpDM_2000_50_10_signal"    :['signal','ZpDM-2000-50-10_signal',1,1]
                  ,"ZpDM_2500_150_10_signal"    :['signal','ZpDM-2500-150-10_signal',1,1]
                  ,"ZpDM_3000_150_10_signal"    :['signal','ZpDM-3000-150-10_signal',1,1]
                  ,"ZpDM_3000_50_10_signal"    :['signal','ZpDM-3000-50-10_signal',1,1]
                  ,"ZpDM_300_150_10_signal"    :['signal','ZpDM-300-150-10_signal',1,1]

		  # Di muon-Control
#                  ,"VH_zmm"                    :['dimuon','vh',1,0] 
                  ,"Zll_zmm"	               :['dimuon','zll',1,1]
 		  ,"Wlv_zmm"      	       :['dimuon','wjets',1,0]
		  ,"Diboson_zmm"    	       :['dimuon','dibosons',1,0]
		  ,"ttbar_zmm"    	       :['dimuon','ttbar',1,0]
		  ,"ST_zmm"                    :['dimuon','stop',1,0]
		  ,"QCD_zmm"		       :['dimuon','qcd',1,0]
		  ,"Data_zmm"    	       :['dimuon','data',0,0]
		  # Single muon (top) control
#                  ,"VH_tm"                     :['singlemuontop','vh',1,0] 
#                  ,"ttH_tm"                    :['singlemuontop','tth',1,0] 
                  ,"Zll_tmn"       	       :['singlemuontop','zll',1,0]
 		  ,"Wlv_tmn"                    :['singlemuontop','wjets',1,0]
		  ,"Diboson_tmn"                :['singlemuontop','dibosons',1,0]
		  ,"ttbar_tmn"                  :['singlemuontop','ttbar',1,1]
		  ,"ST_tmn"                     :['singlemuontop','stop',1,0]
		  ,"QCD_tmn"                    :['singlemuontop','qcd',1,0]
		  ,"Data_tmn"        	       :['singlemuontop','data',0,0]

                   # Single muon (w) control
#                  ,"VH_wmn"                    :['singlemuonw','vh',1,0] 
                  ,"Zll_wmn"     	       :['singlemuonw','zll',1,0]
 		  ,"Wlv_wmn"      	       :['singlemuonw','wjets',1,0]
		  ,"Diboson_wmn"               :['singlemuonw','dibosons',1,0]
		  ,"ttbar_wmn"                 :['singlemuonw','ttbar',1,0]
		  ,"ST_wmn"                    :['singlemuonw','stop',1,0]
		  ,"QCD_wmn"	               :['singlemuonw','qcd',1,0]
		  ,"Data_wmn"	               :['singlemuonw','data',0,0]

		  # Di electron-Control
#                  ,"VH_zee"                    :['dielectron','vh',1,0] 
                  ,"Zll_zee"	               :['dielectron','zll',1,0]
 		  ,"Wlv_zee"  	               :['dielectron','wjets',1,0]
		  ,"Diboson_zee"               :['dielectron','dibosons',1,0]
		  ,"ttbar_zee"                 :['dielectron','ttbar',1,0]
		  ,"ST_zee"                    :['dielectron','stop',1,0]
		  ,"QCD_zee"                   :['dielectron','qcd',1,0]
		  ,"Data_zee"	               :['dielectron','data',0,0]


		  # Single electron (top) control
#                  ,"VH_te"                     :['singleelectrontop','vh',1,0] 
#                  ,"ttH_te"                    :['singleelectrontop','tth',1,0] 
                  ,"Zll_ten"                    :['singleelectrontop','zll',1,0]
                  ,"Wlv_ten"                    :['singleelectrontop','wjets',1,0]
		  ,"Diboson_ten"                :['singleelectrontop','dibosons',1,0]
		  ,"ttbar_ten"                  :['singleelectrontop','ttbar',1,0]
		  ,"ST_ten"                     :['singleelectrontop','stop',1,0]
		  ,"QCD_ten"                    :['singleelectrontop','qcd',1,0]
		  ,"Data_ten"                   :['singleelectrontop','data',0,0]

                   # Single electron (w) control
#                  ,"VH_wen"                    :['singleelectronw','vh',1,0] 
                  ,"Zll_wen"                   :['singleelectronw','zll',1,0]
 		  ,"Wlv_wen"                   :['singleelectronw','wjets',1,0]
		  ,"Diboson_wen"               :['singleelectronw','dibosons',1,0]
		  ,"ttbar_wen"                 :['singleelectronw','ttbar',1,0]
		  ,"ST_wen"                    :['singleelectronw','stop',1,0]
		  ,"QCD_wen"                   :['singleelectronw','qcd',1,0]
		  ,"Data_wen"                  :['singleelectronw','data',0,0]
                  }

}
#monojet_0tag_category = monojet_category["0tag"]
#monojet_1tag_category = monojet_category["1tag"]
#monojet_2tag_category = monojet_category["2tag"]
categories = [monojet_category['0tag'], monojet_category['1tag'], monojet_category['2tag']]
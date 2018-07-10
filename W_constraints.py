import ROOT
from counting_experiment import *
# Define how a control region(s) transfer is made by defining cmodel provide, the calling pattern must be unchanged!
# First define simple string which will be used for the datacard 
model = "wjets"
convertHistograms = []

### helper functions ###

def makeW(cid,_fOut,newName,targetmc,controlmc,systs=None,doSJ=False):
  WScales = targetmc.Clone(); WScales.SetName(newName+"_weights_%s"%cid)
  WScales.Divide(controlmc)
  _fOut.WriteTObject(WScales)

  if not(systs==None):
    for uncert in ['btag','mistag']:
      WScalesUp = systs['targetmc%sUp'%(uncert)].Clone(); 
      WScalesUp.SetName(newName+"_weights_%s_%s_Up"%(cid,uncert))
      WScalesUp.Divide(systs['controlmc%sUp'%(uncert)])

      WScalesDown = systs['targetmc%sDown'%(uncert)].Clone(); WScalesDown.SetName(newName+"_weights_%s_%s_Down"%(cid,uncert))
      WScalesDown.Divide(systs['controlmc%sDown'%(uncert)])

      _fOut.WriteTObject(WScalesUp)
      _fOut.WriteTObject(WScalesDown)

  return WScales


def addWErrors(WScales,targetmc,newName,crName,_fOut,CRs,nCR,cid,doBtag=True):

  if doBtag:
    uncerts = ['btag','mistag']
    for uncert in uncerts:
      CRs[nCR].add_nuisance_shape(uncert,_fOut)

  bins = range(targetmc.GetNbinsX())

  for b in bins:
    err = WScales.GetBinError(b+1)
    '''
    if err > WScales.GetBinContent(b+1):
      err = WScales.GetBinContent(b+1)-0.00001
      print "BIN CONTENT: " + str(WScales.GetBinContent(b+1))
      print "BIN ERROR: " + str(WScales.GetBinError(b+1))
      print "NEW ERROR: " + str(err)
    '''
    if not WScales.GetBinContent(b+1)>0: continue 
    else: relerr = err/WScales.GetBinContent(b+1)
    if relerr<0.001: continue
    byb_u = WScales.Clone(); byb_u.SetName("%s_weights_%s_%s_stat_error_%sCR_bin%d_Up"%(newName,cid,cid,crName,b))
    byb_u.SetBinContent(b+1,WScales.GetBinContent(b+1)+err)
    byb_d = WScales.Clone(); byb_d.SetName("%s_weights_%s_%s_stat_error_%sCR_bin%d_Down"%(newName,cid,cid,crName,b))
    byb_d.SetBinContent(b+1,WScales.GetBinContent(b+1)-err)
    _fOut.WriteTObject(byb_u)
    _fOut.WriteTObject(byb_d)
    CRs[nCR].add_nuisance_shape("%s_stat_error_%sCR_bin%d"%(cid,crName,b),_fOut)


def cmodel(cid,nam,_f,_fOut, out_ws, diag):
  # Some setup
  _fin = _f.Get("category_%s"%cid)
  _wspace = _fin.Get("wspace_%s"%cid)

  # ############################ USER DEFINED ###########################################################
  # First define the nominal transfer factors (histograms of signal/control, usually MC 
  # note there are many tools available inside include/diagonalize.h for you to make 
  # special datasets/histograms representing these and systematic effects 
  # but for now this is just kept simple 
  processName = "WJets" # Give a name of the process being modelled
  mtname = "mT"    # Observable variable name 

  targetmc     = _fin.Get("signalm_wjets")      # define monimal (MC) of which process this config will model
  targetmc_e     = _fin.Get("signale_wjets")
  controlmc    = _fin.Get("singlemuonw_wjets")
  controlmc_e  = _fin.Get("singleelectronw_wjets")
 

  systs = {}; systs_e = {}

  # btag systs
  systs['targetmcbtagUp']      = _fin.Get("signalm_wjets_btagUp");           systs_e['targetmcbtagUp']      = _fin.Get("signale_wjets_btagUp") 
  systs['targetmcbtagDown']    = _fin.Get("signalm_wjets_btagDown");         systs_e['targetmcbtagDown']    = _fin.Get("signale_wjets_btagDown")
  systs['controlmcbtagUp']     = _fin.Get("singlemuonw_wjets_btagUp");    systs_e['controlmcbtagUp']     = _fin.Get("singleelectronw_wjets_btagUp")
  systs['controlmcbtagDown']   = _fin.Get("singlemuonw_wjets_btagDown");  systs_e['controlmcbtagDown']   = _fin.Get("singleelectronw_wjets_btagDown")

  # mistag systs
  systs['targetmcmistagUp']      = _fin.Get("signalm_wjets_mistagUp");           systs_e['targetmcmistagUp']      = _fin.Get("signale_wjets_mistagUp")
  systs['targetmcmistagDown']    = _fin.Get("signalm_wjets_mistagDown");         systs_e['targetmcmistagDown']    = _fin.Get("signale_wjets_mistagDown")
  systs['controlmcmistagUp']     = _fin.Get("singlemuonw_wjets_mistagUp");    systs_e['controlmcmistagUp']     = _fin.Get("singleelectronw_wjets_mistagUp")
  systs['controlmcmistagDown']   = _fin.Get("singlemuonw_wjets_mistagDown");  systs_e['controlmcmistagDown']   = _fin.Get("singleelectronw_wjets_mistagDown")

  # Create the transfer factors and save them (not here you can also create systematic variations of these 
  # transfer factors (named with extention _sysname_Up/Down

  WScales      = makeW(cid,_fOut,"wmn",targetmc,controlmc,systs,False)
  WScales_e    = makeW(cid,_fOut,"wen",targetmc_e,controlmc_e,systs_e,False)


  #######################################################################################################

  _bins = []  # take bins from some histogram, can choose anything but this is easy 
  for b in range(targetmc.GetNbinsX()+1):
    _bins.append(targetmc.GetBinLowEdge(b+1))

  # Here is the important bit which "Builds" the control region, make a list of control regions which 
  # are constraining this process, each "Channel" is created with ...
  # 	(name,_wspace,out_ws,cid+'_'+model,TRANSFERFACTORS) 
  # the second and third arguments can be left unchanged, the others instead must be set
  # TRANSFERFACTORS are what is created above, eg WScales

  CRs = [
   Channel("singlemuonwModel",      _wspace,out_ws,cid+'_'+model,WScales),
   Channel("singleelectronwModel",  _wspace,out_ws,cid+'_'+model,WScales_e),
  ]


  # ############################ USER DEFINED ###########################################################
  # Add systematics in the following, for normalisations use name, relative size (0.01 --> 1%)
  # for shapes use add_nuisance_shape with (name,_fOut)
  # note, the code will LOOK for something called NOMINAL_name_Up and NOMINAL_name_Down, where NOMINAL=WScales.GetName()
  # these must be created and writted to the same dirctory as the nominal (fDir)
  
  addWErrors(WScales,    targetmc,"wmn", "singlemuonwModel",     _fOut,CRs,0,cid)
  addWErrors(WScales_e,  targetmc_e,"wen", "singleelectronwModel", _fOut,CRs,1,cid)

  #######################################################################################################

  cat = Category(model,cid,nam,_fin,_fOut,_wspace,out_ws,_bins,mtname,targetmc.GetName(),CRs,diag)
  #cat.setDependant("zjets","wjetsdependant")  # Can use this to state that the "BASE" of this is already dependant on another process
  # EG if the W->lv in signal is dependant on the Z->vv and then the W->mv is depenant on W->lv, then 
  # give the arguments model,channel name from the config which defines the Z->vv => W->lv map! 
  # Return of course
  return cat


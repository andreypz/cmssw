import FWCore.ParameterSet.Config as cms

from Configuration.Eras.ModifierChain_run2_2017_noTrackingModifier_cff import run2_2017_noTrackingModifier
from Configuration.Eras.Modifier_trackingPhase1_cff import trackingPhase1

Run2_2017_trackingPhase1CA = cms.ModifierChain(run2_2017_noTrackingModifier, trackingPhase1)

import FWCore.ParameterSet.Config as cms

NanoAODEDMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        "keep nanoaodFlatTable_*Table_*_*",     # event data
        "keep edmTriggerResults_*_*_*",  # event data
        "keep String_*_genModel_*",  # generator model data
        "keep nanoaodMergeableCounterTable_*Table_*_*", # accumulated per/run or per/lumi data
        "keep nanoaodUniqueString_nanoMetadata_*_*",   # basic metadata
    )
)


NanoAODjetEventContent = cms.PSet(
  # Data for jet-energy regression training
    outputCommands = cms.untracked.vstring(
      'drop *',
      "keep nanoaodFlatTable_*jet*Table_*_*",
      "keep nanoaodFlatTable_*Jet*Table_*_*",
      "keep nanoaodFlatTable_EnergyRingsTable_*_*",
      "keep nanoaodFlatTable_rhoTable_*_*",
      "keep nanoaodFlatTable_vertexTable_*_*",
      "keep nanoaodFlatTable_genWeightsTable_*_*",
      "keep nanoaodFlatTable_puTable_*_*",
      "keep nanoaodFlatTable_metTable_*_*",
      "keep nanoaodFlatTable_genParticleTable_*_*",
      "keep nanoaodUniqueString_nanoMetadata_*_*",
      "drop nanoaodFlatTable_*fatJetTable_*_*",
    )
)

NANOAODEventContent = NanoAODEDMEventContent.clone(
    compressionLevel = cms.untracked.int32(9),
    compressionAlgorithm = cms.untracked.string("LZMA"),
)
NANOAODSIMEventContent = NanoAODEDMEventContent.clone(
    compressionLevel = cms.untracked.int32(9),
    compressionAlgorithm = cms.untracked.string("LZMA"),
)

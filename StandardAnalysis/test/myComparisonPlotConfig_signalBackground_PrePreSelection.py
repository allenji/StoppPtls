input_sources = [
  { 'condor_dir' : 'PrePreSelection_gluino1200',
    'dataset' : 'GluinoToGChi0_1200_200',
    'channel' : 'StoppedParticlesSelection',
    'legend_entry' : '#tilde{g}#rightarrow g#tilde{#chi}^{0} m_{#tilde{g}}=1200GeV, m_{#tilde{#chi}^{0}}=200GeV',
    'color' : 'blue',
    'fill'  : 'solid',
    'marker' : 'triangle',
    },
  #{ 'condor_dir' : 'PrePreSelection_gluino1200',
    #'dataset' : 'GluinoToGChi0_1200_600',
    #'channel' : 'StoppedParticlesSelection',
    #'legend_entry' : '#tilde{g}#rightarrow g#tilde{#chi}^{0} m_{#tilde{g}}=1200GeV, m_{#tilde{#chi}^{0}}=600GeV',
    #'color' : 'red',
    #'fill'  : 'solid',
    #'marker' : 'circle',
    #},
  { 'condor_dir' : 'PrePreSelection_gluino1200',
    'dataset' : 'GluinoToGChi0_1200_1000',
    'channel' : 'StoppedParticlesSelection',
    'legend_entry' : '#tilde{g}#rightarrow g#tilde{#chi}^{0} m_{#tilde{g}}=1200GeV, m_{#tilde{#chi}^{0}}=1000GeV',
    'color' : 'green',
    'fill'  : 'solid',
    'marker' : 'square',
    },
  { 'condor_dir' : 'PrePreSelection_data',
    'dataset' : 'NoBPTX_2015D',
    'channel' : 'StoppedParticlesSelection',
    'legend_entry' : 'Data passing trigger, BX veto, vertex veto',
    'color' : 'black',
    'fill'  : 'solid',
    'marker' : 'circle',
    },
]

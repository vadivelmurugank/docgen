from seqdiag import parser, builder, drawer

diagram_definition = u"""
   seqdiag {
      CDiagScript -> CDiagScript;
      CDiagFunc -> CDiagFunc;
      DTP -> CRpCard [label="<new>"];
      CRpCard -> DiagFe1600  [label="<new> Spanky2Fe1600, FE0, FE1"];
      CRpCard -> DiagFe1600  [label="<new> Shiba2Fe1600 , FE0, FE1"];
      DiagSpanky2RegisterDevice <- DiagFe1600  [label="<Spanky2FE1600>, Name, CardType"];
      DiagFe1600  -> DiagFe1600  [label="<< new >>"];
      Spanky2Fe1600 <- DiagFe1600  [label="Init, devid" ];
      Spanky2Fe1600 -> Spanky2Fe1600 [label="Initialze Spanky2 FE1600"];
      DiagFe1600  -> Spanky2Fe1600 [label="GetDeviceBaseAddress(<DevId>)"];
      Spanky2Fe1600 -> DiagFe1600  [label="FE0/1 Mapped BAR Address"];
      DiagFe1600  -> BCM-SDK [ label="bcm driver init"];
      BCM-SDK -> BCM-SDK [label="CM SAL Init"];
      BCM-SDK -> BCM-SDK [label="Device Attach"];
      BCM-SDK -> BCM-SDK [label="soc_reset_Init"];
      BCM-SDK -> BCM-SDK [label="bcm_init"];
      DiagShiba2RegisterDevice <- DiagFe1600  [label = "<Shiba2FE1600>, Name, CardType"];
      DiagFe1600  -> DiagFe1600  [label="<< new >>"];
      Shiba2Fe1600 <- DiagFe1600  [ label="Init, devid" ];
      Shiba2Fe1600 -> Shiba2Fe1600 [ label="Initialze Shiba2 FE1600"];
      DiagFe1600  -> Shiba2Fe1600 [label="GetDeviceBaseAddress(<DevId>)"];
      Shiba2Fe1600 -> DiagFe1600  [label="FE0/1 Mapped BAR Address"];
      DiagFe1600  -> BCM-SDK [ label="bcm driver init"];
      BCM-SDK -> BCM-SDK [label="CM SAL Init"];
      BCM-SDK -> BCM-SDK [label="Device Attach"];
      BCM-SDK -> BCM-SDK [label="soc_reset_Init"];
      BCM-SDK -> BCM-SDK [label="bcm_init"];

      CDiagScript -> CDiagFunc   [label="<< Call Fe1600 Function >"];
      CDiagFunc -> DiagFe1600  [label="dev-reset"];
      CDiagFunc -> DiagFe1600  [label="dev-init"];
      CDiagFunc -> DiagFe1600  [label="get-avs"];
      CDiagFunc -> DiagFe1600  [label="pll-rst-on"];
      CDiagFunc -> DiagFe1600  [label="pll-rst-off"];
      CDiagFunc -> DiagFe1600  [label="pll-status"];
      CDiagFunc -> DiagFe1600  [label="snake-test"];
      CDiagFunc -> DiagFe1600  [label="prbs-test"];
      CDiagFunc -> DiagFe1600  [label="fabric_tuning"];
      CDiagFunc -> DiagFe1600  [label="fabric-stats"];
   
    } """

tree = parser.parse_string(diagram_definition)
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="fe1600-seqdiag.png")
draw.draw()
draw.save()


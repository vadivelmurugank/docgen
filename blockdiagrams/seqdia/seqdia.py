from seqdiag import parser, builder, drawer

diagram_definition = u"""
   seqdiag {

        // Set edge metrix.
        //edge_length = 300;  // default value is 192
        //span_height = 580;  // default value is 40
        //span_width = 1580;  // default value is 40

        // Set fontsize.
        default_fontsize = 16;  // default value is 11

        // Do not show activity line
        //activation = none;

        // Numbering edges automaticaly
        autonumber = False;

        // Change note color
        default_note_color = lightgrey;

      browser  -> webserver [label = "GET /index.html"];
      browser <- webserver;
      browser -> browser [label = "Loop inside"];
   }
"""
tree = parser.parse_string(diagram_definition)
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="diagram.png")
draw.draw()
draw.save()


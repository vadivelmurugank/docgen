
from seqdiag import parser, builder, drawer


# sphinx extension
#.. seqdiag::
#
#    seqdiag admin {
#      A -> B -> C;
#    }


seq_diagram_definition = u"""
   seqdiag {

    // order of elements
    Card1; Card2; browser; webserver; runblock; init

    //edge_length = 300;
    //span_height = 80;
    default_fontsize = 12;
    autonumber = true;
    default_note_color = "lightblue";
    
    // no activity line
    //activation = none;

    // Nester Init Routines
    init => runblock [label = "Call", return = "Return status"]
        runblock => Card1 [label = "Card Init", return = "Status"]
        Card1 => browser [label = "Start Web", return = "status"]

      === Card To Card ===
      Card1 -> Card2 [note = "request", label = "<new label> "];
      Card2 -> Card1 [rightnote = "Response back", label = "new label", textcolor="red" ];
      ... Card To Web Server ...
      browser <- Card1 [diagonal, label="Card1-Card3"];
      browser  -> webserver [label = "GET /index.html"];
      browser <- webserver;
      browser <- webserver [label="failed request", failed]
      browser -> browser [label = "Loop inside"];
   }
"""

seq_tree = parser.parse_string(seq_diagram_definition)
seq_diagram = builder.ScreenNodeBuilder.build(seq_tree)
seq_draw = drawer.DiagramDraw('PNG', seq_diagram, filename="seq-diagram.png")
seq_draw.draw()
seq_draw.save()

from seqdiag import parser, builder, drawer

diagram_definition = u"""
    seqdiag {
    // Set edge metrix.
    //  edge_length = 300;  // default value is 192
    //  span_height = 80;  // default value is 40
      span_width = 380;  // default value is 40

      // Set fontsize.
      //default_fontsize = 36;  // default value is 11

      // Do not show activity line
      //activation = none;

      // Numbering edges automaticaly
      //autonumber = True;

      // Change note color
      //default_note_color = lightblue;
        
        Caldera-IDEFIX -> RP [label="Telnet to RP"];
        === RP Configuration ===
        RP -> RP [note = "Configure RP SSH Server sshd_config for Alive Interval and Modes"];
        RP -> RP [note = "Generate keys: ssh-keygen -v -N -f /root/.ssh/id_rsa"];
        RP -> RP [note = "Remove Existing Authorized Keys and hosts"];
        === RP to LC ===
        RP --> LC [diagonal, label = "Verify SSH connection from RP to LC"];
         RP -> LC [label= "Copy RP Public key to LC", note="ssh-copy-id -i /root/.ssh/id_rsa.pub"];
        RP -> LC [label = "Passwordless Connection" note="ssh -v -o ServerAliveInterval=10 -o ServerAliveCountMax=20 ", color=blue];
        === LC Configuration ===
        LC -> LC [note = "Configure LC SSH server sshd_config for Alive Intervals"];
        LC -> LC [label = "Generate keys", note="ssh-keygen -v -N -f /root/.ssh/id_rsa"];
        === LC to RP ===
        LC -> RP [label = "Copy LC Public key to RP", note="ssh-copy-id -i /root/.ssh/id_rsa.pub"];
        LC --> RP [diagonal, label = "Verify SSH connection from LC to RP"];
        LC -> RP [label = "Passwordless Connection", note="scp files from RP to LC", color=blue];
   }
"""
tree = parser.parse_string(diagram_definition)
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="SSH-Passwordless.png")
draw.draw()
draw.save()

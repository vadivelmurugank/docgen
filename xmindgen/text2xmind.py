import lxml
from mekk.xmind import XMindDocument
import re, os

debug = 0
# Debug Prints
def dprint(*args):
    if debug: 
        for arg in args: print(arg,)

def derror(*args):
    print ("ERROR>> ",)
    for arg in args: print(arg,)

# colors=["palegreen", "lightblue", ...]
colors=["#98fb98", "#8ddae6", "", "", "", "", "", ""]

class text2xmind():
    """
    Convert formatted text to xmind using XMindDocument
    The formatted text has the tab spaces to specify xmind mindmap nodes.
    """

    def __init__(self, textfile):
        self.textfile = textfile
        with open(self.textfile) as fd:
            self.fstr=fd.read()

    def get_xmind_attr(self, tagstr):
        note=topstr=notestr=lnkstr=""
        topstr = re.split("::", tagstr,1)
        tagstr=topstr[0]
        if (len(topstr) > 1): 
            note =re.split("\(.*!", topstr[1],1)
            if (len(note) > 1): 
                notestr=note[0]
                lnkstr=re.split("\)",note[1],1)[0]
            else:
                notestr = topstr[1]

        # Delete text start markers "*", "-", "+" 
        if (re.match('^\s*[\*|\-|\+]\s*',tagstr)):
            #tagstr1=re.split('^\s*[\*|\-|\+]\s*',tagstr)
            tagstr=re.sub('[\*|\-|\+]+','',tagstr,1)
        
        attr = {"topic" : tagstr, 
                "note"  : notestr,
                "link"  : lnkstr}
        return attr
        

    def convert2xmind(self, xmindfile=''):
        """
        - Read from the text file and convert of list of string tokens
        - Read the string tokens and parse it 
        - Create Abstract tree with all nodes.
        - Convert nodes to mindmap nodes
        """
        # read the text contents
        lstr=re.split(r'\n', self.fstr.strip())
        whitespace=re.compile(r'^\s+')

        node=[[]]
        level = 0
        OUTPUT = ""
        dprint(lstr)
        for tagstr in lstr:
            if not tagstr: continue
            if (re.match('^\s*$',tagstr)) : continue
            if (re.match('^\s*[\#]\s*',tagstr)): continue
            match=whitespace.search(tagstr)
            if not match: 
                level=0
                if (len(node) > 2):
                    xmind.save(OUTPUT)
                    print("Saved to", os.path.join(os.getcwd(),OUTPUT))
                    if (OUTPUT): OUTPUT=""
                    node=[[]]
            else:
                level = int(len(match.group()) / 4)
                last = level-1

            if not node[level]:
                node.append([])

            self.attr=self.get_xmind_attr(tagstr)
            tagstr  = self.attr["topic"]
            notestr = self.attr["note"]
            lnkstr  = self.attr["link"]

            if tagstr: dprint(tagstr)
            if notestr: dprint("::",notestr)
            if lnkstr: dprint("!", lnkstr)

            if (level == 0):
                OUTPUT = tagstr+".xmind"
                OUTPUT.strip()
                xmind = XMindDocument.create(tagstr, tagstr)
                first_sheet = xmind.get_first_sheet()
                topic = first_sheet.get_root_topic()
                subtopic = topic
                topicstyle = xmind.create_topic_style(fill=colors[level])
                subtopic.set_style(topicstyle)
            elif node[last]:
                topic = node[last][len(node[last])-1][0]
                subtopic = topic.add_subtopic(self.attr["topic"])

            if notestr: subtopic.set_note(notestr)
            if lnkstr : subtopic.set_link(lnkstr)
            if level < len(colors) and level == 1:
                topicstyle = xmind.create_topic_style(fill=colors[level])
                                            #shape="SHAPE_ROUND_RECTANGLE")
                subtopic.set_style(topicstyle)
            node[level].append([subtopic])
            dprint(level, ":", node[level])

            if ((level > 0) and node[last]):
                node[last][len(node[last])-1].append([len(node[level])-1])
                dprint("prev:", node[last])

        dprint('-'*60)
        dprint(len(node), range(len(node)-1))
        dprint(node)
        dprint("-----")
        for start_index in range(len(node)-2):
            dprint("len ==>",  range(len(node[start_index])))
            for next_index in range(len(node[start_index])):
                dprint(start_index, "==>",  node[start_index][next_index][0])
                for elem in range(1,len(node[start_index][next_index])):
                    dprint ("@:", node[start_index][next_index][elem][0])
                    dprint ("@@@:", node[start_index+1][node[start_index][next_index][elem][0]][0])
        
        if (len(node) > 1):
            xmind.save(OUTPUT)
            print("Saved to", os.path.join(os.getcwd(),OUTPUT))
       
        if debug: 
            xmind.pretty_print()


if __name__ == "__main__":
    import sys
        
    usage = "%prog <formatted text file>"
    if (len(sys.argv) < 2):
        sys.exit(usage)

    textfile = sys.argv[1]
    
    mindmap = text2xmind(sys.argv[1])
    mindmap.convert2xmind()


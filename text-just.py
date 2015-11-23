import pdb

class Solution:
    def makeline(self, line, slen, L, last=False):
        if last:
            ret=" ".join(line)
            ret+=" "*(L-len(ret))
            return ret
        if L==slen-1:
            return " ".join(line)
        truelen=sum(map(len,line))
        if len(line)==1:
            return line[0]+" "*(L-truelen)
        blanknum=L-truelen
        averageb=blanknum/(len(line)-1)
        remind=blanknum%(len(line)-1)
        blanks=[averageb+1]*remind+[averageb]*(len(line)-1-remind)
        ret=line[0]
        for i in range(len(blanks)):
            ret+=" "*blanks[i]
            ret+=line[i+1]
        return ret
        
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res=[]
        line=[]
        slen=0
        #pdb.set_trace()
        for i in range(len(words)-1):
            if slen + len(words[i]) <= L:
                line.append(words[i])
                slen+=len(words[i])+1
                continue
            res.append(self.makeline(line,slen,L))
            line=[words[i]]
            slen=len(words[i])+1
        if slen+len(words[-1])>L:
            res.append(self.makeline(line,slen,L))
            res.append(self.makeline([words[-1]],len(words[-1])+1,L,True))
        else:
            line.append(words[-1])
            slen+=len(words[-1])+1
            res.append(self.makeline(line,slen,L,True))
        return res
s=Solution()
print s.fullJustify(["What","must","be","shall","be."], 12)
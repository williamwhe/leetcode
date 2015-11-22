class Solution(object):
    def geweishu(self, num):
        retval=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        return retval[num-1]
    
    def shiweishu(self, num):
        retval=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        return retval[num-2]
    
    def tens(self, num):
        retval=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        return retval[num]
    
    def yibaiyinei(self, num):
        retval=[]
        if num>=100:
            retval.append(self.geweishu(num/100)+" Hundred")
            num%=100
        if num>=10:
            if num/10==1:
                retval.append(self.tens(num%10))
                return " ".join(retval)
            
            retval.append(self.shiweishu(num/10))
            num%=10
        if num>0:
            retval.append(self.geweishu(num))
        return " ".join(retval)
    
    def numberToWords(self, num):
        if num==0:
            return "Zero"
        retval=[]
        if num>=1000000000:
            billion=self.yibaiyinei(num/1000000000)
            if billion!="":
                retval.append(billion+" Billion")
            num%=1000000000
        if num>=1000000:
            million=self.yibaiyinei(num/1000000)
            if million!="":
                retval.append(million+" Million")
            num%=1000000
        if num>=1000:
            thousand=self.yibaiyinei(num/1000)
            if thousand!="":
                retval.append(thousand+" Thousand")
            num%=1000
        rest=self.yibaiyinei(num)
        if rest!="":
            retval.append(rest)
        return " ".join(retval)
    
s=Solution()
print s.numberToWords(1000)
print s.numberToWords(0)
print s.numberToWords(123)
print s.numberToWords(12345)
print s.numberToWords(1234567)
print s.numberToWords(2**31-1)
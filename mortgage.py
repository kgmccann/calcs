
class Mortgage:
    def __init__(self,assessment_rate=0.636,max_leverage_rate=0.45):
        self.assessment_rate = assessment_rate
        self.max_leverage_rate = max_leverage_rate
    
    def approximate_max_purchase_price(self,income,outflow,interest,millage,term=30,ho_ins=0.0035,pmi=0.0004,tol=.01):
        p,p1=0,500000
        assessment_rate = self.assessment_rate
        max_leverage_rate = self.max_leverage_rate
        i= interest/12
        n=term*12
        #p_list = [p1] 
        while abs(p1-p)>tol:
            p=p1
            p1 =  (max_leverage_rate-(outflow + ho_ins * (p/.95)/12 + pmi * (p/.95) + (assessment_rate*p*millage/1000)/12)/(income/12))*(income/12)*((i+1)**n-1)/(i*(i+1)**n)      
            #p_list.append(p1)
        print(f'Monthly Taxes: {round((assessment_rate*p*millage/1000)/12)}')
        print(f'Monthly Home-owners Insurance: {round(ho_ins * (p/.95)/12)}')
        print(f'Down Payment: {round(.05*p1)}')
        return round(p1/.95), round((max_leverage_rate-(outflow + ho_ins * (p/.95)/12 + pmi * (p/.95) + (assessment_rate*p*millage/1000)/12)/(income/12))*(income/12))#,p_list
mortgage = Mortgage()
#mortgage.approximate_max_purchase_price(100000,2400,.05,23.49)

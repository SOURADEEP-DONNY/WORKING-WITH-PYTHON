# CLASS AND METHOD WORKINGS
#===============================================================================
class working_practice_class():
    def __init__(self,factory_name,factory_racking,sales,profit):
        self.factory_name=factory_name
        self.factory_ranking=factory_racking
        self.sales=sales
        self.__calculation()  #METHOD ENCAPSULATION
    def __calculation(self):
        self.profit=0.1*self.sales
    def display(self):
        print('NAME OF THE COMPANY IS',self.factory_name)
        print('RANKING OF THE COMPANY IS',self.factory_ranking)
        print('SALES OF THE FACTORY IS',self.sales)
        print('PROFIT OF THE COMPANY IS',self.profit)

#CREATING AN OBJECT FOR THE CLASS.
object1=working_practice_class('BMW',20,5000000009,0)
object1.display()


#WHEN WE HAVE TO CALCULATE SOMETHING IN ANOTHER METHOD OTHER THAN '__init__'
# METHOD, THEN METHOD ENCAPSULATION IS USED. HERE THE '__method' CAN ONLY BE
# CALLED BY THE __init__ METHOD.

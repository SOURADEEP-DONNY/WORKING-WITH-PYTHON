class FoodItem:
    def __init__(self,item_id,item_name,item_category,item_price):
        self.item_id=item_id
        self.item_name=item_name
        self.item_category=item_category
        self.item_price=item_price

    def provideDiscount(self,dis_per):
        updated_price=item_price-((dis_per/100)*item_price)
        return updated_price

class Restaurant:
    def __init__(self,fooditem_list):
        self.fooditem_list=fooditem_list

    def retrieveUpdatedPrice(self,updated_per,Id):
        l=[]
        for i in fooditem_list:
            if i.item_id==Id:
                l.append(i.item_name)
                l.append(i.item_price-((updated_per/100)*i.item_price))
                return l
        return None

if __name__=='__main__':
    n=int(input())
    fooditem_list=[]
    for i in range(n):
        item_id=int(input())
        item_name=input()
        item_category=input()
        item_price=int(input())
        b=FoodItem(item_id,item_name,item_category,item_price)
        fooditem_list.append(b)
    obj=Restaurant(fooditem_list)
    Id=int(input())
    updated_price=int(input())
    r1=obj.retrieveUpdatedPrice(updated_price,Id)
    print(r1[0]+'-'+str(r1[1]))

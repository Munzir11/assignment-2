#List of cars available and their prices
cars={"jeep trakhawk":10000,"toyota Camry":400000,"toyota rav":550000,"toyota vitz":580000, \
"toyota highlander":450000,"rangerover evoque":500000,"toyota fortuner":5450000,"benz gle":600000, \
"lexus lx43":542000,"bugati veyron":780000,"bmw x7":340000,"bmw x5":690000,"bmw j5":400000,     
"lexus es350":657000,"rangerover vogue":700000,"benz e43":130000,"benz glc300":320000,      
"benz gle 350":6100000,"bmw m5":880000,"lamborghini urus":200000,"benz glc 300":800000, \
"lamborgini aventador":999000,"bugati chiron":990000,"pagani hyuara":1000000,"toyota vibe":1000000, \
"mclarenspeedtail":150000,"bugatti divo":2000000,"lexus lx600":2500000,"lexus i350":3000000, \
"lamborgini hurucan":3560000,"bmw m8 grnd coupe":4000000,"toyota prado":4760000,"nissan g3":5000000, \
"lamborghini aventidor svj5":5450000,"lexus lx530":6000000,"rangerover sport":6540000,      
"nissan patrol":7000000}
# get user input for car name
CarName= input('please enter car name:')
#check if car name is in the list of available cars
if CarName in cars:
    print('yes please')
    #if car name is present,get its price
    CarPrice= cars[CarName]
    print(f'the priceof {CarName} is ${CarPrice}.')
else:
    #if car name is not present, inform the user
    print('sorry, {CarName} is not available.')    

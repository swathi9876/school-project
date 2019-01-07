import time
print('Welcome to Mad Libs Theatre')
k=input('Enter your genre from these options:a.Weird or b.Funny Crime: ')
if k=='a':
    a=input('Are You Ready(y/n):')
    while a!='n':
        adjective1=input('Enter an adjective:')
        adjective2=input('Enter an adjective:')
        adjective3=input('Enter an adjective:')
        adjective4=input('Enter an adjective:')
        adjective5=input('Enter an adjective:')
        adjective6=input('Enter an adjective:')
        adjective7=input('Enter an adjective:')
        adjective8=input('Enter an adjective:')
        noun1=input('Enter a noun:')
        noun2=input('Enter a noun:')
        noun3=input('Enter a noun:')
        noun4=input('Enter a noun:')
        noun5=input('Enter a noun:')
        noun6=input('Enter a noun:')
        noun7=input('Enter a noun:')
        clothing1=input('Enter an item of clothing:')
        noise1=input('Enter a noise:')
        noise2=input('Enter a noise:')
        foreignname=input('Enter a foreign name:')
        bodypart1=input('Enter a body part:')
        bodypart2=input('Enter a body part:')
        colour1=input('Enter a colour:')
        colour2=input('Enter a colour:')
        liquid=input('Enter a liquid:')
        exclamation1=input('Enter an exclamation that you use often:')
        exclamation2=input('Enter an exclamation that you use often:')
        animal1=input('Enter the name of an animal:')
        animal2=input('Enter the name of another animal:')
        num1=input('Enter a number:')
        num2=input('Enter another number:')
        adverb1=input('Enter an adverb:')
        adverb2=input('Enter an adverb:')
        adverb3=input('Enter an adverb:')
        petsname=input('Enter a pets name:')
        print()
        print()
        print()
        time.sleep(3.5)
        print('I will never forget the night it happened.')
        time.sleep(3.2)
        print('It was a(n)',adjective1,'night., and I was relaxing upstairs with my',noun1,'a good book and my faithful',animal1,'', petsname,'. Suddenly there was a loud ',noise1,'. ')
        time.sleep(3.5)
        print(' I sprang to my feet and crept downstairs, trying to be as',adjective2,'as I could. Nothing looked out of the ordinary. Suddenly I heard the',noise1,'again, but this time it was much more',adjective3,'and I knew it was coming from the basement.' )
        time.sleep(3)
        print('Summoning my courage, I grabbed a flashlight and strode ',adverb1,'down the stairs. I might have met my end right there, if not for',petsname,',who let out a loud "',noise2,'!" Startled, I jumped',adverb2,'to the side just in time to avoid a long gooey appendage. I turned my flashlight on the intruder and gasped in horror. ')
        time.sleep(3)
        print('Lurking there in my basement, bathed in the',adjective4,'glow of my light, was a huge, quivering, shapeless blob of ooze! The hideous thing was as',colour1,'as a',noun2,'and as big as a(n)',noun3,'."',exclamation2,'"I cried.')
        time.sleep(3)
        print('I fled',adverb3,'upstairs, but the thing chased me with lightning speed. I was trapped, and knew I had to fight if I wanted to survive. First I tried to chop it with a',adjective7,'',noun4,'from the kitchen, then I shot it with my grandpas',noun5,'that hangs over the fireplace. In desperation, I even tried throwing',liquid,'on it, but all to no avail. It just kept coming. I thought I was dead for sure, when suddenly a strange figure crashed through my window and leapt between us!')
        time.sleep(4)
        print(' He was tall and',adjective5,',with fierce long eyes and sharp shoulders. He was dressed entirely in black, except for his',colour2,'',clothing1,'."',exclamation1,'"the figure cried, and quick as a(n)',animal2,'he jumped in and stunned the ooze creature with a powerful kick.Without pause he scooped the thing into a(n)',noun6,'and tied it shut with a ',adjective6,'',noun7,'.')
        time.sleep(3.5)
        print('"How did you do that?!" I gasped, trying to catch my breath."Their only weakness is their',bodypart1,',"he replied. "One good kick and the things are helpless.""But how do you find it?" I asked, staring at the shapeless mass."That is easy," said the stranger. "It is right next to their',bodypart2,'."')
        time.sleep(3)
        print('I thanked him for saving my life and asked him his name. "I am',foreignname,',and I have been hunting the ooze creatures all my life. Join me in my quest and we will make the world safe from their',adjective8,' evil!"')
        time.sleep(3)
        print('Now that I knew the truth, how could I say no? I joined',foreignname,'that night and my life has never been the same. I learned how to spot their',bodypart1,'in less than',num1,'seconds, and together we have defeated over',num2,'of the ooze creatures. I even got my own',colour2,clothing1,'.')
        time.sleep(3)
        
        a=input('Again?(y/n)?:')
elif k=='b':
    a=input('Are You Ready(y/n):')
    while a!='n':
        malename=input('Enter male name:')
        teachername=input('Enter a teachers name:')
        exclamation1=input('Enter an exclamation:')
        exclamation2=input('Enter a silly word:')
        num2=input('Enter a number:')
        storename=input('Enter the name of a store:')
        plural2=input('Enter plural object..(eg.eggs):')
        body2=input('Enter a body part:')
        holiday=input('Enter the name of a holiday:')
        verb2=input('Enter verb ending in -ing:')
        movie=input('Enter a movie title:')
        length=input('Enter an amount of distance:')
        country=input('Enter the name of a country:')
        pet=input('Enter a pet animal:')
        quote=input('Enter a famous movie quote:')
        bodypart2=input('Enter another body part:')
        childrensong=input('Enter the name of a childrens song:')
        adjective=input('Enter an adjective:')
        print()
        print()
        print()
        print()
        time.sleep(3)
        print("*knocks on table*...Hello!....I'm detective",malename,"...and you are?")
        time.sleep(3)
        print(teachername)
        time.sleep(3)
        print("You're here today under suspicion of 2nd degree robbery.....")
        time.sleep(3)
        print(exclamation1,"!!!!")
        time.sleep(3)
        print("That's right...",num2,"",plural2,"were stolen from",storename,"and the crime scene has your",body2,"written all over it.")
        time.sleep(3.5)
        print(exclamation2,"!!!!")
        time.sleep(3)
        print("Where were you on the night of",holiday,"?")
        time.sleep(3)
        print("I was watching",movie,"")
        time.sleep(3)
        print("Then why does the crime scene footage show you",verb2," just",length,"away from the crime scene?.......I'm through with playing games....Where are you from?!")
        time.sleep(4.5)
        print(country)
        time.sleep(3)
        print("..Yeah..You know the best part about being a detective is that I get to go home to my children and pet",pet,"after locking up criminals like you and say",quote,"")
        time.sleep(3.5)
        print("Fine...I did it..I commited the robbery but I only did it because I needed the money for my",bodypart2,"surgery")
        time.sleep(3)
        print("I knew it all along...I knew it all along and every time I catch bastards like you I like to sing my favouraite song",childrensong,"")
        time.sleep(3)
        print("Wow....You have a",adjective,"voice!...I love you!")
        time.sleep(3)
        a=input('Again?(y/n)?:')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
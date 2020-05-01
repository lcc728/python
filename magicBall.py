# Magic Ball
#https://www.george.tw/
import random

# https://zh.wikipedia.org/wiki/神奇八號球
magicMap={
      1:'It is certain (這是必然)',
      2:'It is decidedly so  (肯定是的)',
      3:'Without a doubt  (不用懷疑)',
      4:'Yes, definitely  (毫無疑問)',
      5:'You may rely on it  (你能依靠它)',
      6:'As I see it, yes  (如我所見，是的)',
      7:'Most likely  (很有可能)',
      8:'Outlook good  (外表很好)',
      9:'Yes  (是的)',
      10:'Signs point to yes  (種種跡象指出「是的」)',
      11:'Reply hazy try again  (回覆攏統，再試試)',
      12:'Ask again later  (待會再問)',
      13:'Better not tell you now  (最好現在不告訴你)',
      14:'Cannot predict now  (現在無法預測)',
      15:'Concentrate and ask again  (專心再問一遍)',
      16:'Don\'t count on it  (想的美)',
      17:'My reply is no  (我的回覆是「不」)',
      18:'My sources say no  (我的來源說「不」)',
      19:'Outlook not so good  (外表不太好)',
      20:'Very doubtful  (很可疑)'
}

while True:
   question=input("Enter your question:")
   magicNum = random.randint(1,20)
   print("Your question  =>" + question)
   print("My answer =>" + magicMap[magicNum])
   if (magicNum > 16 or magicNum < 11):
         break
      





             


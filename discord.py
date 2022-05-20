import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!서버이름"))

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕 만나서 반가워")

@bot.command()
async def 사용방법(ctx):
    await ctx.send("! 서버이름 ")

@bot.command()
async def 하제(ctx):
    try: 
        아키하제response = requests.get("https://archeage.xlgames.com/play/worldinfo/HAJE")
        아키하제response.encoding = 'utf-8'
        아키하제html = 아키하제response.text
        soup = BeautifulSoup(아키하제html, 'html.parser')

        아키하제정보 = soup.select('.bond-info')

        서_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(1) > td > ul')
        서_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(2) > td > ul')
        서_목재 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(3) > td > ul')
        서_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(4) > td > ul')

        동_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(1) > td > ul')
        동_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(2) > td > ul')
        동_목재 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(3) > td > ul')
        동_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(4) > td > ul')

        await ctx.send(f'누이아 대륙')
        for 옷감 in 서_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 서_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 서_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 서_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')  

        await ctx.send(f'하리하라 대륙')
        for 옷감 in 동_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 동_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 동_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 동_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')        
    except:
        await ctx.send(f'--출력 오류--')

@bot.command()
async def 누이(ctx):
    try: 
        아키하제response = requests.get("https://archeage.xlgames.com/play/worldinfo/NUI")
        아키하제response.encoding = 'utf-8'
        아키하제html = 아키하제response.text
        soup = BeautifulSoup(아키하제html, 'html.parser')

        아키하제정보 = soup.select('.bond-info')

        서_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(1) > td > ul')
        서_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(2) > td > ul')
        서_목재 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(3) > td > ul')
        서_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(4) > td > ul')

        동_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(1) > td > ul')
        동_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(2) > td > ul')
        동_목재 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(3) > td > ul')
        동_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(4) > td > ul')

        await ctx.send(f'누이아 대륙')
        for 옷감 in 서_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 서_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 서_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 서_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')  

        await ctx.send(f'하리하라 대륙')
        for 옷감 in 동_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 동_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 동_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 동_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')        
    except:
        await ctx.send(f'--출력 오류--')

@bot.command()
async def 다후타(ctx):
    try: 
        아키하제response = requests.get("https://archeage.xlgames.com/play/worldinfo/DAHUTA")
        아키하제response.encoding = 'utf-8'
        아키하제html = 아키하제response.text
        soup = BeautifulSoup(아키하제html, 'html.parser')

        아키하제정보 = soup.select('.bond-info')

        서_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(1) > td > ul')
        서_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(2) > td > ul')
        서_목재 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(3) > td > ul')
        서_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(4) > td > ul')

        동_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(1) > td > ul')
        동_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(2) > td > ul')
        동_목재 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(3) > td > ul')
        동_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(4) > td > ul')

        await ctx.send(f'누이아 대륙')
        for 옷감 in 서_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 서_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 서_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 서_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')  

        await ctx.send(f'하리하라 대륙')
        for 옷감 in 동_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 동_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 동_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 동_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')        
    except:
        await ctx.send(f'--출력 오류--')

@bot.command()
async def 랑그레이(ctx):
    try: 
        아키하제response = requests.get("https://archeage.xlgames.com/play/worldinfo/RANGORA")
        아키하제response.encoding = 'utf-8'
        아키하제html = 아키하제response.text
        soup = BeautifulSoup(아키하제html, 'html.parser')

        아키하제정보 = soup.select('.bond-info')

        서_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(1) > td > ul')
        서_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(2) > td > ul')
        서_목재 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(3) > td > ul')
        서_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(4) > td > ul')

        동_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(1) > td > ul')
        동_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(2) > td > ul')
        동_목재 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(3) > td > ul')
        동_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(4) > td > ul')

        await ctx.send(f'누이아 대륙')
        for 옷감 in 서_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 서_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 서_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 서_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')  

        await ctx.send(f'하리하라 대륙')
        for 옷감 in 동_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 동_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 동_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 동_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')        
    except:
        await ctx.send(f'--출력 오류--')

@bot.command()
async def 에버나이트(ctx):
    try: 
        아키하제response = requests.get("https://archeage.xlgames.com/play/worldinfo/EVERNIGHT")
        아키하제response.encoding = 'utf-8'
        아키하제html = 아키하제response.text
        soup = BeautifulSoup(아키하제html, 'html.parser')

        아키하제정보 = soup.select('.bond-info')

        서_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(1) > td > ul')
        서_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(2) > td > ul')
        서_목재 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(3) > td > ul')
        서_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table:nth-child(1) > tbody > tr:nth-child(4) > td > ul')

        동_옷감 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(1) > td > ul')
        동_가죽 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(2) > td > ul')
        동_목재 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(3) > td > ul')
        동_철주괴 = soup.select('#container-common > div > div > div > div.bond-info > table.table-bond.right > tbody > tr:nth-child(4) > td > ul')

        await ctx.send(f'누이아 대륙')
        for 옷감 in 서_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 서_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 서_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 서_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')  

        await ctx.send(f'하리하라 대륙')
        for 옷감 in 동_옷감:
            await ctx.send(f'```옷감{옷감.text}\n```')    
        for 가죽 in 동_가죽:
            await ctx.send(f'```가죽{가죽.text}\n```')
        for 목재 in 동_목재:
            await ctx.send(f'```목재{목재.text}\n```') 
        for 철주괴 in 동_철주괴:
            await ctx.send(f'```철 주괴{철주괴.text}\n```')        
    except:
        await ctx.send(f'--출력 오류--')
bot.run("OTc2NTkxMjM0MTY2NTcxMDU4.G8SxA8.HXW7_epuo8KlwTBWn3pu_jbMjT0W-aX2SK45Jg")
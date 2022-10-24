from telethon import events
from .. import loader, utils
from asyncio import sleep
import random

a = """•"""
ab = """••"""
abc = """•••"""

__version__ = (1, 0, 0)

# meta developer: @iNetUz
# meta channel: @umodules

def register(cb):
	cb(OvozMemlarMod())
	
class OvozMemlarMod(loader.Module):
	"""Qiziqarli ovoz memlar🔊"""
	
	strings = {
		"name": "@iNetUz - Ovoz Memlar🥷🏻",
		}

	async def ovozcmd(self, message):
		"""Ovoz Memlar Ro'yxati"""
		
		royhat = """
<i>📖Buyruqlarning tartib roʻyhati:</i>

<code>.assalom</code> - <b>✨Assalomaleykum 😊</b>
<code>.group</code> - <b>💫Gurpa uchun😆</b>
<code>.jigarlarim</code> - <b>💫Jigarlarim✊</b>
<code>.qarz</code> - <b>💫Qarzini beer🤑</b>
<code>.odam</code> - <b>💫Odam qoshdim👥</b>
<code>.sigaret</code> - <b>💫Brat sigaret bormi🚬</b>
<code>.nimabovoti</code> - <b>💫Nima bovotti🗣</b> <code>.qaytaylik</code> - <b>💫Uyga qaytaylik😃</b>
<code>.uy</code> - <b>💫Uyga qaytaylik😃</b>
<code>.yerdumaloq</code> - <b>💫Yer dumaloq bopladimmi😉</b>
<code>.mol</code> - <b>💫Mol, eshak🐂</b>
<code>.pul</code> - <b>💫Pul kebqosade😅</b>
<code>.barsa</code> - <b>💫Barsachilar😄</b>
<code>.yashash</code> - <b>💫Yashash yaxshi😄</b>
<code>.kocha</code> - <b>💫Qishloqda ham ko'cha bor📌</b>
<code>.uzb</code> - <b>💫O'zbekni bolasi😜</b>
<code>.otiramiz</code> - <b>💫Qachon o'tiramiz😄</b>
<code>.oylapman</code> - <b>💫Sizlarni odam deb o'ylabman😝</b>
<code>.yopaman</code> - <b>💫Gurpani yopaman💣</b> 
<code>.xa</code> - <b>✨Xa shunaqa degin😏</b>
<code>.erkak</code> - <b>✨Biz Erkak Kishimiz🤵‍♂</b>
<code>.tilinga</code> - <b>✨ Tilinga Shakar Ukajonim 👅</b>
<code>.maslahat</code> - <b>💫Uylanganlarga maslahat😍</b>
<code>.gapizga</code> - <b>✨ Shu Gapizga Manavuni 😜</b>
<code>.oila</code> - <b>💫Oila boqqan yaxshi👏</b> <code>.kampir</code> - <b>💫Kampirim👵</b>
<code>.kampir</code> - <b>💫Kampirim👵</b>
<code>.money</code> - <b>💫Pul🤑</b>
<code>.kallang</code> - <b>💫Kallang bormi🤦‍♂</b>
<code>.oyog</code> - <b>💫Oyog'ini urib sindiraman😳</b>
<code>.yoqol</code> - <b>💫yoqol betdan😝</b>
<code>.som</code> - <b>💫50ming🌝</b>
<code>.choyxona</code> - <b>💫Choyxonaga kelib turing😅</b>
<code>.kimbore</code> - <b>💫Kimbore😜</b>
<code>.qanioila</code> - <b>💫Qani olila😁</b>
<code>.meni</code> - <b>✨ Meni Aytyapdi 😅</b>
<code>.humkalla</code> - <b>✨ Ke Humkalla 😀</b>
<code>.boy</code> - <b>✨ Faqat Men Boy Bo'lay 🤣</b>
<code>.indan</code> - <b>✨ Indan keyinchi 😏</b>
<code>.kalxoz</code> - <b>✨ San Qaysi Kalxozdansan 🤔</b>
<code>.yaxshi</code> - <b>✨ Yaxshi Qolilar😅</b>
<code>.tarqal</code> - <b>✨Tarqal Tarqal 🚨</b>
<code>.jona</code> - <b>✨Jo'na Buyerdan🤨</b>
<code>.ohno</code> - <b>✨ Oh no Oh no 😝</b>
<code>.yoqol</code> - <b>✨ Yoqol Hammang 😀</b>
<code>.eta</code> - <b>✨Eta Shahlohon😲</b>
<code>.xatosi</code> - <b>✨Dushmanlarimni xatosi🤭</b>
<code>.kulish</code> - <b>✨Qotib Qotib Kulish😄</b>
<code>.rostan</code> - <b>✨ Rostan Seryozni 😂</b>
<code>.birkecha</code> - <b>✨ Bir Kecha Mexmoning Bo'lay 😅</b>
<code>.erkak2</code> - <b>✨ Ha Erkak Erkak 😁</b> <code>.salom</code> - <b>✨ Salam Alaykum ☺️</b>
<code>.salom </code> - <b>✨ Salam Alaykum ☺️</b>
<code>.uxla</code> - <b>✨ Uxlaa 😀</b>
<code>.mazami</code> - <b>✨ Mazami Silaga Mazami 😄</b>
<code>.kimbor</code> - <b>✨ Kim Bor E 🗣</b>
<code>.auf</code> - <b>✨ Auf 😎</b>
<code>.boldi</code> - <b>✨Boldi Bas Qil Uxla 🤨</b>
<code>.mazgi</code> - <b>✨ Mazgii 😂</b>
<code>.kulish2</code> - <b>✨ Sokin Kulish 😃</b>
<code>.erkak3</code> - <b>✨ Pasportiga Erkak Deb Yozgan 😂</b>
<code>.soska</code> - <b>Soskani qizi😁😂😂</b>
<code>.xuy</code> - <b>Qoʻtoq orzu qilasan 😂😂😂</b>
<code>.chort</code> - <b>Choʻrt 😂😂🤦‍♂</b>
<code>.yaloq</code> - <b>Om yaloq😋</b>
<code>.yaloq</code> - <b>Rasmga ol Rasmga ol</b>

<i>Yangi ovoz memlar hali oldinda...</i>

<b>🥷🏻Yaratuvchi:</b> @iNetUz
<b>📖Kanalimiz:</b> @UModules"""
		await message.edit(royhat)
		return

	async def assalomcmd(self, message):
		"""✨Assalomaleykum 😊"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/7", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def groupcmd(self, message):
		"""💫Gurpa uchun😆"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/8", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def jigarlarimcmd(self, message):
		"""💫Jigarlarim✊"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/10", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def qarzcmd(self, message):
		"""💫Qarzini beer🤑"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/11", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def odamcmd(self, message):
		"""💫Odam qoshdim👥"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/12", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def sigaretcmd(self, message):
		"""💫Brat sigaret bormi🚬"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/13", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def nimabovoticmd(self, message):
		"""💫Nima bovotti🗣"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/15", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def uycmd(self, message):
		"""💫Uyga qaytaylik😃"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/16", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yerdumoloqcmd(self, message):
		"""💫Yer dumaloq bopladimmi😉"""
		
		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/17", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def molcmd(self, message):
		"""💫Mol, eshak🐂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/18", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def pulcmd(self, message):
		"""💫Pul kebqosade😅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/19", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def barsacmd(self, message):
		"""💫Barsachilar😄"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/20", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yaxshicmd(self, message):
		"""💫Yashash yaxshi😄"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/21", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kochacmd(self, message):
		"""💫Qishloqda ham ko'cha bor📌"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/22", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def uzbcmd(self, message):
		"""💫O'zbekni bolasi😜"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/23", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def otiramizcmd(self, message):
		"""💫Qachon o'tiramiz😄"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/24", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def oylabmancmd(self, message):
		"""💫Sizlarni odam deb o'ylabman😝"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/25", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yopamancmd(self, message):
		"""💫Gurpani yopaman💣"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/26", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def xacmd(self, message):
		"""✨Xa shunaqa degin😏"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/27", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def erkakcmd(self, message):
		"""✨Biz Erkak Kishimiz🤵‍♂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/28", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def tilingacmd(self, message):
		"""✨ Tilinga Shakar Ukajonim 👅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/29", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def maslahatcmd(self, message):
		"""💫Uylanganlarga maslahat😍"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/30", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def gapizgacmd(self, message):
		"""✨ Shu Gapizga Manavuni 😜"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/31", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def oilacmd(self, message):
		"""💫Oila boqqan yaxshi👏"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/32", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kampircmd(self, message):
		"""💫Kampirim👵"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/33", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def moneycmd(self, message):
		"""💫Pul🤑"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/34", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kallangcmd(self, message):
		"""💫Kallang bormi🤦‍♂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/35", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def oyogcmd(self, message):
		"""💫Oyog'ini urib sindiraman😳"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/36", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yoqolcmd(self, message):
		"""💫yoqol betdan😝"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/37", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def somcmd(self, message):
		"""💫50ming🌝"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/38", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def choyxonacmd(self, message):
		"""💫Choyxonaga kelib turing😅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/39", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kimborecmd(self, message):
		"""💫Kimbore😜"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/40", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def qanioilacmd(self, message):
		"""💫Qani olila😁 """

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/41", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def menicmd(self, message):
		"""✨ Meni Aytyapdi 😅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/42", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def humkallacmd(self, message):
		"""✨ Ke Humkalla 😀"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/43", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def boycmd(self, message):
		"""✨ Faqat Men Boy Bo'lay 🤣"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/44", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def indancmd(self, message):
		"""✨ Indan keyinchi 😏"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/45", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kalxozcmd(self, message):
		"""✨ San Qaysi Kalxozdansan 🤔"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/46", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yaxshicmd(self, message):
		"""✨ Yaxshi Qolilar😅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/47", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def tarqalcmd(self, message):
		"""✨Tarqal Tarqal 🚨"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/48", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def jonacmd(self, message):
		"""✨Jo'na Buyerdan🤨"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/49", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def ohnocmd(self, message):
		"""✨ Oh no Oh no 😝"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/50", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yoqolcmd(self, message):
		"""✨ Yoqol Hammang 😀"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/53", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def etacmd(self, message):
		"""✨Eta Shahlohon😲?"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/54", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def xatosicmd(self, message):
		"""✨Dushmanlarimni xatosi🤭"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/55", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kulishcmd(self, message):
		"""✨Qotib Qotib Kulish😄"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/56", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def rostancmd(self, message):
		"""✨ Rostan Seryozni 😂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/57", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def birkechacmd(self, message):
		"""✨ Bir Kecha Mexmoning Bo'lay 😅"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/58", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def erkak2cmd(self, message):
		"""✨ Ha Erkak Erkak 😁"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/59", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def salomcmd(self, message):
		"""✨ Salam Alaykum ☺️"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/60", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def uxlacmd(self, message):
		"""✨ Uxlaa 😀"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/61", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def mazamicmd(self, message):
		"""✨ Mazami Silaga Mazami 😄"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/62", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kimborcmd(self, message):
		"""✨ Kim Bor E 🗣"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/63", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def aufcmd(self, message):
		"""✨ Auf 😎"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/64", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def boldicmd(self, message):
		"""✨Boldi Bas Qil Uxla 🤨"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/65", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def mazgicmd(self, message):
		"""✨ Mazgii 😂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/66", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def kulish2cmd(self, message):
		"""✨ Sokin Kulish 😃"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/67", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def erkak3cmd(self, message):
		"""✨ Pasportiga Erkak Deb Yozgan 😂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/68", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def soskacmd(self, message):
		"""Soskani qizi😁😂😂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/69", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def xuycmd(self, message):
		"""Qoʻtoq orzu qilasan 😂😂😂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/70", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def chortcmd(self, message):
		"""Choʻrt 😂😂🤦‍♂"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/71", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def yaloqcmd(self, message):
		"""Om yaloq😋"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/72", voice_note=True, reply_to=reply.id if reply else None)
		return
		
	async def rasmcmd(self, message):
		"""Rasmga ol Rasmga ol"""

		reply = await message.get_reply_message()
		await message.edit(a)
		await sleep(0.1)
		await message.edit(ab)
		await sleep(0.1)
		await message.edit(abc)
		await sleep(0.1)
		await message.delete()
		await message.client.send_file(message.to_id, "https://t.me/iNetUzMods/73", voice_note=True, reply_to=reply.id if reply else None)
		return
		
		
		
		
		
		

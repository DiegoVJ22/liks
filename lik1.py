from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(17932927)
    api_hash = "ae4b6a81deaf452abeacf454bc47bd60"
    phone_number = "51991980747"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@SPAMLEO", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4226213709")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@SPAMLEO", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["PERÚ VENTAS🔥","Compra y Venta Shadow","🇵🇪MARKETPLACE PERÚ (FOCOMUNDO) 🌏🔥📈","VENTAS LIMA (BIENES Y SERVICIOS)","Mercado libre / Iquitos","🔵Miraflores ✨Compra y venta💲","COMPRA Y VENTA TRUJILLO","CIENEGUILLA MERCADO LIBRE","👨🏻‍💻 🇵🇪 COMUNIDAD EFSOCIETY 🇵🇪 👨🏻‍💻","Cuba Compra/Ventas","Compra Venta Paypal Facebook Binance Usdt","Compra y Venta Miraflores 💵","México Compras Y Ventas","COMPRAS Y VENTAS EN CUSCO😁","Perú Empleos","Perú Ventas","Perú Anuncios","Venta de cuentas Netflix Perú","YAPETON","🍿𝚅𝙴𝙽𝚃𝙰𝚂 Ñ𝙾𝙵𝙸𝚂 𝙰𝟷🍿","LA BEBA ARMY DOXING","Perú Compras","CACHINA, COMPRA, VENDE MOQUEGUA 🛒","💻 Metaverso Streaming Perú 🇵🇪","APPS FAKE","DoxeoPremium","Referencias Lik7","COMISIONISTA APPS FAKE","VENDEDORES OFICIALES APPS FAKE","SISTEMA DOXEO","DoxPremium","REF. ANABELLE (VENTA OFICIALES)","Yape Fake 2024","ANTHXNYLlNTERNA REFERENCIAS","Killnet","Refererencias Caputin🌩","🔪🩸Jason Vip🩸🔪","FAJOS G5","ACCESO X","REFERENCIAS🇵🇪","ReferenciasCarding","闩ᗪᗪㄩ乂 丂廾ㄖ尸","TernitasPE / Cards","Cuchito army oficial","ʟᴏɢɪɴꜱ ᴘᴇʀú ʀᴇꜰᴇʀᴇɴᴄɪᴀꜱ🇵🇪","REFF BILLETES G5","🫧【𝗡〓𝗕𝗨𝗟𝗔】彡[ʀᴇꜰᴇʀᴇɴᴄɪᴀꜱ]彡","MONITO X","skett referencias メ ✁👾","Sparks Master Card 💻💳💵","1K DE SEGUIDORES CANAL DE TG","AccesosX","Quemando estofadores Rework","Referencias YOVANI 🇵🇪~🇲🇽","EL AMIGO FIEL 2.0","Referencias De Los Papus","꧁༒ᴅᴀʀᴋ ☬ ꜱᴛᴏʀᴇ༒꧂","LAS CHOCO REFERENCIAS 2.0","DetectPe","HimikoData [🎄𝓡𝓼 +]","🇨🇴Compras y Ventas Colombia, Ecuador y México.🇪🇨🇲🇽","Referencias - MickyTouna","Bots :)","spam2024","Spam 2024","RESPALDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.send_message(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@SPAMLEO", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@SPAMLEO", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        await asyncio.sleep(10)
                        if j==6: break
            await client.send_message("@SPAMLEO", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(100) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())
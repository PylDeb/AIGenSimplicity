import assemblyai as aai

aai.settings.api_key = "83afcf647349427aa3c42f9a1e6ad1ca"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://rr2---sn-npoldn7e.googlevideo.com/videoplayback?expire=1717950105&ei=OYJlZuKqNf2ep-oP--2l0AU&ip=82.205.52.252&id=o-AJfSC7K5DMCBojsXq5IU16q_ap-fv77YCay_oq2xTol4&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AbKP-1Nl06Y33Tr1qxA_z_xprL_hV7a5ofZM6i6WqJuYN0wImAi8oBQulhFIVepg649AWMXDxaLz7JMW&vprv=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=3162130&ratebypass=yes&dur=85.333&lmt=1717783199627097&c=MEDIA_CONNECT_FRONTEND&txp=5319224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Cmime%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAL2v2Tr9BkLCf-r1N8dLjkvhnBKaeq5pduLh4NETj9wNAiAfBZkJByYzExpOvuFbT7P2mwhgsKbHQJS71X69n_MApg%3D%3D&title=Moving%20from%20AI%20experimentation%20to%20business%20breakthrough%20%7C%20AI%20at%20work%20with%20Microsoft%27s%20Jared%20Spataro&rm=sn-25auxa-1qhk76&fexp=24350485&req_id=a4c2333c0a81a3ee&cmsv=e&redirect_counter=2&cm2rm=sn-hgnlk7l&cms_redirect=yes&mh=En&mip=103.49.240.141&mm=34&mn=sn-npoldn7e&ms=ltu&mt=1717927943&mv=m&mvi=2&pl=24&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AHlkHjAwRQIgBZ9qoSyaddMuf7RJnx9ezequnxL2ftXIwOENK_UdbjECIQCjOG80JkAs-zA9YHE7KhznBwwzFJCGgMuca_Tf_3LrNA%3D%3D")
# transcript = transcriber.transcribe("./local-file.wav")

print(transcript.text)
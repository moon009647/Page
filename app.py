<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> 🤍 𝙏𝙃𝙀𝙁 𝙇𝙀𝙂𝙀𝙉𝘿 𝘼𝙇𝙄𝙄 𝙓 𝘽𝙍𝘼𝙉𝘿🦋</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    label{ color: white; }
    .file{ height: 30px; }
    body{
        background-image: url(https://sour-tan-jy9uyfjo3e.edgeone.app/00db2575-d012-4611-ada5-027392f02f94.jpeg');
        background-size: cover;
        background-repeat: no-repeat;
        color: white;
    }
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
      border: none;
      resize: none;
    }
    .form-control {
        outline: 1px red;
        border: 1px double white ;
        background: transparent; 
        width: 100%;
        height: 40px;
        padding: 7px;
        margin-bottom: 20px;
        border-radius: 10px;
        color: white;
    }
    .header{ text-align: center; padding-bottom: 20px; }
    .btn-submit{ width: 100%; margin-top: 10px; }
    .footer{ text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link { display: inline-block; color: #25d366; text-decoration: none; margin-top: 10px; }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header mt-4">
  <h1 class="mt-3">𝙏𝙃𝙀𝙁 𝙇𝙀𝙂𝙀𝙉𝘿 𝘼𝙇𝙄𝙄 𝙓 𝘽𝙍𝘼𝙉𝘿</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">𝚂𝙴𝙻𝙴𝙲𝚃 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙵𝙸𝙻𝙴 </label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝙲𝙾𝙽𝚅𝙾 𝙶𝙲/𝙸𝙽𝙱𝙾𝚇 𝙸𝙳</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">H𝙰𝚃𝙷𝙴𝚁 𝙽𝙰𝙼𝙴</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">M𝙸𝙽 𝙳𝙴𝙻𝙰𝚈 (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝚃𝙴𝚇𝚃 𝙵𝙸𝙻𝙴</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">sᴛᴀʀᴛ ɴᴇᴡ ᴛᴀsᴋ</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">sᴛᴏᴘ ᴀʟʟ ᴛᴀsᴋs</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 2026 𝙏𝙃𝙀𝙁 𝙇𝙀𝙂𝙀𝙉𝘿 𝘼𝙇𝙄𝙄 𝙓 𝘽𝙍𝘼𝙉𝘿</p>
    <p><a href="https://www.facebook.com/">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴀʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+923202043776" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
</body>
</html>
    
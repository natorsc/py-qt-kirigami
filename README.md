![Python - PySide - Qt - Kirigami](docs/images/py-qt-kirigami.webp)

<br>

# Python - Qt - Kirigami

Initial template for projects with [Python](https://www.python.org/), [Qt](https://www.qt.io/) framework and [KDE Kirigami](https://develop.kde.org/frameworks/kirigami//).

## 🤓 Author

Repository created with 💙 by [Renato Cruz](https://github.com/natorsc) 🤜🤛 Feel free to reach out!

[![Email](https://img.shields.io/badge/-Email-blueviolet?logo=gmail&logoColor=white)](mailto:natorsc@gmail.com "Send an email.")

Check out programming and technology content on:

[![justcode.com.br](https://img.shields.io/badge/-justcode.com.br-grey?logo=hashnode&logoColor=white)](https://justcode.com.br/ "Visit the justCode blog.")

[![swift.dev.br](https://img.shields.io/badge/-swift.dev.br-orange?logo=hashnode&logoColor=white)](https://justcode.com.br/ "Visit the justCode blog.")

A playlist I often listen to while studying or coding 😁:

[![Spotify](https://img.shields.io/badge/-Spotify-darkgreen?logo=spotify&logoColor=white)](https://open.spotify.com/playlist/1xf3u29puXlnrWO7MsaHL5?si=A-LgwRJXSvOno_e6trpi5w&utm_source=copy-link "Access the playlist.")

---

## 💝 Donations

Thank you for your donation, it's through your support that I can maintain this content 😊.

### Github

https://github.com/sponsors/natorsc/

### Pix (Brazil)

**Key**: `b1839493-2afe-484d-9272-82a3e402b36f`

---

---

## Flatpak pip generator

Tool assists in creating project dependencies

```bash
wget \
https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/master/pip/flatpak-pip-generator \
--directory-prefix .venv/bin
```

```bash
curl --create-dirs -O \
--output-dir .venv/bin/ \
https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/master/pip/flatpak-pip-generator
```

**Example**:

```bash
python \
.venv/bin/flatpak-pip-generator \
markdown
```

---

## Publishing

### Flatpak

#### Dependencies

**KDE**:

```bash
flatpak install \
flathub \
org.kde.Platform/x86_64/6.8 \
org.kde.Sdk/x86_64/6.8
```

**PySide**:

```bash
flatpak install \
flathub \
io.qt.PySide.BaseApp/x86_64/6.8
```

#### Packaging

**Build**:

```bash
flatpak-builder \
--force-clean \
flatpak-build-dir \
br.com.justcode.Qt.json
```

**Run**:

```bash
flatpak-builder \
--run \
flatpak-build-dir \
br.com.justcode.Qt.json \
app-name
```

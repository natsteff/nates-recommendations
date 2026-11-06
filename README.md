# Nate's Recommendations

A collection of things I recommend, including public repositories I’ve starred on GitHub.

## Homelab Recommendations

### Infrastructure

- **Docker** ([Docker Engine for Linux](https://docs.docker.com/engine/install/), [Docker Desktop for Mac, Windows, and Linux](https://docs.docker.com/desktop/)) — Run self-hosted apps in containers. A workstation is a good way to try Docker with hardware you already have, and it can be your main Docker host if you only need apps while that machine is running. For other devices on your network, the workstation needs to stay awake and connected, Docker needs to be running, and the app’s port needs to be published on a reachable interface and allowed through the firewall. An always-on host makes those apps easier to reach reliably. [Docker port publishing](https://docs.docker.com/engine/network/port-publishing/)

- **Proxmox Virtual Environment (VE)** ([official ISO downloads](https://www.proxmox.com/en/downloads/proxmox-virtual-environment)) — Run KVM virtual machines and LXC containers from a web interface. Proxmox VE is open source under AGPLv3 and free to download and use for a personal homelab without a subscription. The no-subscription update repository is available for non-production use. Proxmox’s paid Community subscription adds access to the Enterprise Repository. [Installation and licensing](https://proxmox.com/en/products/proxmox-virtual-environment/get-started) · [Update repositories](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html#sysadmin_package_repositories) · [Subscriptions](https://www.proxmox.com/en/?id=23)

  **Why use a VM for Docker?** You can run Docker on bare metal, but even for a single Docker host, running it in a Proxmox VM makes backup and recovery easier. Proxmox can schedule backups of the VM’s configuration and included virtual disks, then restore them together so you don’t have to rebuild the Docker host by hand. [Proxmox backup and restore](https://pve.proxmox.com/pve-docs/chapter-vzdump.html)

### Docker Host and NAS (Network Attached Storage) Hardware

Docker can run on a compact mini PC, a refurbished desktop, an old gaming rig, or a custom rackmount server. Choose hardware based on what your containers do, how many you run, and how much storage they need. Here are three examples from my own setup.

| Host | My configuration | What it suits |
| --- | --- | --- |
| **Gigabyte BRIX GB-BSi5-6200** | Intel Core i5-6200U (2 cores, 4 threads), 16 GB RAM, 128 GB SSD | Compact, low-power host for lightweight Docker services |
| **Dell OptiPlex 3040** | 16 GB RAM, 1 TB storage | Small to moderate workloads |
| **Dell OptiPlex 3050 Micro** | 32 GB RAM, 4 TB SSD, access to a Synology NAS | Multiple services and storage-intensive apps |

**A NAS makes modest hosts more capable.** Keep media libraries, documents, backups, and other large datasets on network storage. Local disk space is still useful for the operating system, container images, databases, and performance-sensitive app data. That split lets a mini PC with a small internal drive run services that use much larger datasets.

#### NAS

#### Retail Solutions

- **Synology DiskStation DS225+** — A compact two-bay NAS for shared files, media, and backups. The [diskless model](https://a.co/d/06WDfLj9) lets you choose your own compatible drives. The [16 TB bundle](https://a.co/d/0htiYQk6) comes with two 8 TB Seagate IronWolf drives. That's 16 TB of raw capacity, or roughly 8 TB before formatting overhead if you mirror the two drives. [Synology specs and drive compatibility](https://www.synology.com/en-us/products/DS225%2B)
- **QNAP TS-264** — A two-bay NAS with two 2.5GbE ports and two M.2 slots for SSDs. [QNAP specifications](https://www.qnap.com/en-us/product/ts-264/specs/hardware/software)
- **UGREEN NASync DXP2800** — A two-bay NAS for shared storage and backups. [UGREEN product page](https://www.ugreen.com/products/usa-25242)

#### DIY

- **TrueNAS Community Edition** — A free DIY option for a spare PC or a purpose-built NAS. It uses OpenZFS for storage pools and snapshots and can share files with your Docker hosts over the network. [TrueNAS Community Edition](https://www.truenas.com/truenas-community-edition/)
- **openmediavault** — A free, Debian-based DIY option if you mainly want network file shares managed through a web interface. [openmediavault](https://www.openmediavault.org/)
- **Unraid** — A paid option for reusing drives of different sizes and expanding one disk at a time. If you use parity, the parity drive must be at least as large as the largest data drive. [Unraid](https://unraid.net/product/) · [Array expansion docs](https://docs.unraid.net/unraid-os/using-unraid-to/manage-storage/array/adding-disks-to-array/)
- **Debian + Samba** — A straightforward way to share files from a Linux machine you already keep running. You manage the disks and backups yourself. [Debian file-sharing guide](https://wiki.debian.org/Samba/ServerSimple)

Keep a separate backup of anything you can't replace. A drive mirror helps if one drive fails, while a separate backup gives you another copy if files are deleted or the NAS itself is lost.

<!-- github-stars:start -->
### Docker & Self-Hosted Apps

- **Audiobookshelf** ([advplyr/audiobookshelf](https://github.com/advplyr/audiobookshelf)) — Self-hosted audiobook and podcast server
- **Dockpeek** ([dockpeek/dockpeek](https://github.com/dockpeek/dockpeek)) — Easily access your Docker container web interfaces and keep them up to date — across all your hosts.
- **DOSee** ([bengarrett/DOSee](https://github.com/bengarrett/DOSee)) — DOSee is a DOSBox based, MS-DOS emulator for the web.
- **ErsatzTV Legacy** ([ErsatzTV/legacy](https://github.com/ErsatzTV/legacy)) — Open-source platform that transforms your personal media library into live, custom TV channels.
- **ErsatzTV Next** ([ErsatzTV/next](https://github.com/ErsatzTV/next)) — Transcode and stream your media as live TV channels.
- **FORGE GameSheets**\* ([natsteff/forge-gamesheets](https://github.com/natsteff/forge-gamesheets)) — Self-hosted library for organizing, finding, and printing board-game resources.
- **Glances** ([nicolargo/glances](https://github.com/nicolargo/glances)) — Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, macOS and Windows operating systems.
- **Heimdall** ([linuxserver/Heimdall](https://github.com/linuxserver/Heimdall)) — An Application dashboard and launcher
- **HomeBox** ([sysadminsmedia/homebox](https://github.com/sysadminsmedia/homebox)) — A continuation of HomeBox the inventory and organization system built for the Home User
- **Immich** ([immich-app/immich](https://github.com/immich-app/immich)) — High performance self-hosted photo and video management solution.
- **Jellyfin** ([jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)) — The Free Software Media System - Server Backend &amp; API
- **Karakeep** ([karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)) — A self-hostable bookmark-everything app \(links, notes and images\) with AI-based automatic tagging and full text search
- **Kavita** ([Kareadita/Kavita](https://github.com/Kareadita/Kavita)) — Kavita is a fast, feature rich, cross platform reading server. Built with the goal of being a full solution for all your reading needs. Setup your own server and share your reading collection with your friends and family.
- **LocalSend** ([localsend/localsend](https://github.com/localsend/localsend)) — An open-source cross-platform alternative to AirDrop
- **MeTube** ([alexta69/metube](https://github.com/alexta69/metube)) — Self-hosted video downloader for YouTube and other sites \(web UI for yt-dlp\)
- **MySpeed** ([gnmyt/MySpeed](https://github.com/gnmyt/MySpeed)) — A speed test analysis software that shows your internet speed for up to 30 days
- **Nametag** ([mattogodoy/nametag](https://github.com/mattogodoy/nametag)) — A simple, yet effective Personal Relationship Manager
- **Navidrome** ([navidrome/navidrome](https://github.com/navidrome/navidrome)) — 🎧 Your Personal Streaming Service
- **NGINX** ([nginx/nginx](https://github.com/nginx/nginx)) — The official NGINX Open Source repository.
- **Paperless-ngx** ([paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)) — A community-supported supercharged document management system: scan, index and archive all your documents
- **PeaNUT** ([Brandawg93/PeaNUT](https://github.com/Brandawg93/PeaNUT)) — A tiny dashboard for Network UPS Tools
- **Pi-hole** ([pi-hole/pi-hole](https://github.com/pi-hole/pi-hole)) — A black hole for Internet advertisements
- **Portainer** ([portainer/portainer](https://github.com/portainer/portainer)) — Making Docker and Kubernetes management easy.
- **RomM** ([rommapp/romm](https://github.com/rommapp/romm)) — A beautiful, powerful, self-hosted ROM manager and player.
- **Scratch Map** ([ad3m3r5/scratch-map](https://github.com/ad3m3r5/scratch-map)) — An open-source scratch-off style map to track your travels.
- **Uptime Kuma** ([louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)) — A fancy self-hosted monitoring tool
- **Vikunja** ([go-vikunja/vikunja](https://github.com/go-vikunja/vikunja)) — The task manager you actually own.
- **Wallos** ([ellite/Wallos](https://github.com/ellite/Wallos)) — Wallos: Open-source, self-hostable personal subscription tracker. Visualize your recurring expenses, manage your budget, and save money.
- **What’s Up Docker?** ([getwud/wud](https://github.com/getwud/wud)) — Keep your containers up-to-date\!
- **Yamtrack** ([FuzzyGrim/Yamtrack](https://github.com/FuzzyGrim/Yamtrack)) — A self hosted media tracker.

## Desktop & Mobile Apps

- **SARGE Desktop**\* ([natsteff/SARGE-Desktop](https://github.com/natsteff/SARGE-Desktop)) — SARGE Desktop Beta: Windows photo inventory, offline catalogs, RAW/export matching and verified copy workflows. AGPL-3.0.
- **Shelf Elf Librarian**\* ([natsteff/shelf-elf-librarian](https://github.com/natsteff/shelf-elf-librarian)) — Shelf Elf Librarian — native macOS filename preparation and library filing alpha
- **TagCraft**\* ([natsteff/TagCraft](https://github.com/natsteff/TagCraft)) — macOS MP3 tag editor and music library organizer with Magic, filename tools, playback, statistics and health reports. Currently in Beta.

## Web Apps

- **FGS Studio**\* ([natsteff/FGS-Studio](https://github.com/natsteff/FGS-Studio)) — A hosted alternative to FORGE GameSheets. Create and edit board game \(or similar\) game sheets in your browser and export them as FGS or PDF. No account required.

## Browser Games

- **Lil G in Eau Claire**\* ([natsteff/lil-g-in-eau-claire](https://github.com/natsteff/lil-g-in-eau-claire)) — Browser platformer starring Lil’ G, with mobile support using customizable controls. Dodge traffic &amp; unique characters to deliver a towering stack of beer across Eau Claire with selectable custom music soundtrack.
- **Seth Happens\! A New Adventure**\* ([natsteff/seth-happens-a-new-adventure](https://github.com/natsteff/seth-happens-a-new-adventure)) — Seth Happens - A New Adventure: early alpha arcade platforming across eight adventures.

\* Shameless Self-Promotion

Last successful sync that changed this list (UTC) · 2026-11-06
<!-- github-stars:end -->

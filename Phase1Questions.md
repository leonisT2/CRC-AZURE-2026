## Phase 1 Questions

### Most difficult aspect's of Chunk 1?
- This was understanding exactly how the individual pieces listed below, fit together.
    - index.html file
    - static website primary endpoint
    - Cloudflare (TXT and CNAME record)
    - Origin group and origin hostname
    - Front Door endpoint
    - Custom Domain

### Note one or two challanges that one overcame to get the static site deployed
- Got a QueryParameterName: comp error when I thought I had correctly configured the origin hostname. I was pointing the raw blob storage endpoint instead of the static website primary endpoint. I kept thinking about which endpoint/link was actually serving my website which led me to change Storage (Azure blobs) to Storage (Static Website) as the origing type and change the hostname(origin hostname) which in essence, the custom domain correctly points to

- CNAME records. With a quick google search of what they are, I understood that I needed to make a reference between my custom domain name and the Front Door endpoint hostname that is routed to the origin group holding the static website primary endpoint.

### What's something done differently or added if one had more time?
- CRC challange ask to use CDN classic but that is no longer available in Azure so I pivoted and used Azure Front Door Standard instead.  

### If one of the mods was attempted, note what was done and how it improved over the basic challange requirements
- To be attempted.
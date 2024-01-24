    function showAnimation(duration = 5000){ //hi
    const template = `
    <div id="animation-loading" style="z-index: 1040 !important;width: 100%; height: 100vh" class="wrapper position-fixed top-0 end-0 start-0 end-0">
    <svg style="z-index: 1050 !important;">
        <text x="50%" y="50%" dy=".100em" text-anchor="middle" class="text-center display-1">
        </text>
    </svg>
    </div>
`
    document.body.innerHTML = template + document.body.innerHTML
        window.setTimeout(e => {
            document.querySelector("#animation-loading").classList.add("hide")
            window.setTimeout(event => {
                document.querySelector("#animation-loading").remove()
            }, 1100)
        }, duration)
    }
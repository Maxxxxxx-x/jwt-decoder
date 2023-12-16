<script lang="ts">
    import { verify, decode } from "@tsndr/cloudflare-worker-jwt";
    import { fade } from "svelte/transition"; 

    let secret : string = "your secret here"
    let b64encoded : boolean = false;
   
    let token : string;
    let running : boolean = false;
    let isValid : boolean;
    let isVerified : boolean = false;

    let header : string;
    let payload : string;

    async function verifyToken() {
        let tmpSecret = secret;
        if (b64encoded) {
            tmpSecret= btoa(tmpSecret);
        }
        isVerified = await verify(token, tmpSecret)
    }

    async function decodeToken() : Promise<void> {
        running = true;
        try {
            token = token.replace(/\s/g, "");
            const decodedToken =decode(token);
            isValid = true;
            header = JSON.stringify(decodedToken.header, null, 4);
            payload = JSON.stringify(decodedToken.payload, null, 4);
             await verifyToken();
        } catch {
            isValid = false;
        } finally {
            running = false
        }
    }

</script>

<svelte:head>
</svelte:head>

<div class="flex flex-col h-screen items-center justify-center bg-white gap-y-20">
    <div class="flex flex-col justify-center items-center w-full">
        <label class="font-bold text-3xl" for="">jwt decoder</label>
    </div>
    <div class="flex flex-row justify-center items-center gap-x-5 w-full px-96 h-100">
        <div class="flex flex-col justify-start rounded-xl border p-7 w-full h-full gap-y-5">
            <label class="font-bold text-2xl text-center" for="">Encoded Token</label>
            <textarea class="textarea textarea-bordered textarea-ghost textarea-lg h-80" tabindex="0" spellcheck="false" autocorrect="off" placeholder="Enter your token here" bind:value={token} on:keyup={decodeToken} />
        </div>
        {#if token}
            <div class="justify-center divider divider-horizontal" transition:fade={{ duration:100 }}/>
            {#if running === false && isValid === true }
            <div class="flex flex-col justify-end rounded-xl border p-7 w-full h-full gap-y-5" transition:fade={{ duration: 100 }}>
                <label class="font-bold text-2xl text-center" for="">Decoded Token</label>
                <div class="flex flex-col justify-evenly">
                    <div class="flex flex-col border">
                        <label class="border" for="">Header: Algorithm & Token Type</label>
                        <textarea class="textarea textarea-bordered textarea-ghost textarea-lg h-20" bind:value={header} disabled />
                    </div>
                    <div class="flex flex-col border">
                        <label class="border" for="">Payload: Data</label>
                        <textarea class="textarea textarea-bordered textarea-ghost textarea-lg h-20" bind:value={payload} disabled />
                    </div>
                    <div class="flex flex-col border">
                        <label class="border" for="">Verify Signature</label>
                        <input class="input input-bordered input-ghost" bind:value={secret} on:keyup={verifyToken}>
                        <div class="flex flex-row">
                            <input id="b64encoded" class="checkbox checkbox-md checkbox-info" type="checkbox" bind:checked={b64encoded} on:change={verifyToken} />
                            <label for="b64encoded">base64-encoded secret</label>
                        </div>
                    </div>
                    {#if isVerified}
                        <p class="text-center text-3xl text-success">Signature Verified</p>
                    {:else}
                            <p class="text-center text-3xl text-error">Invalid Signature</p>
                        {/if}
                    </div>
                </div>
            {:else}
                <div class="flex flex-col justify-center rounded-xl border p-7 w-full h-full gap-y-5" transition:fade={{ duration:100 }}>
                    <p class="text-center text-3xl text-error">Invalid Token</p>
                </div>
            {/if}
        {/if}
    </div>
</div>

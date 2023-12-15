<script lang="ts">
    import { page } from "$app/stores";
</script>


<svelte:head>
    <title>Error | jwt-decoder</title>
</svelte:head>


<div class="flex flex-col justify-center items-center h-screen -top-5">
    <h1 class="font-bold text-3xl">Hmmm....  Looks like an error occured!</h1>
    <h2 class="font-bold text-lg">Error {$page.status} | {$page.error?.message}</h2>
    <div class="flex flex-row mt-5 gap-5">
        <a class="btn btn-md btn-primary" href="/">Go back</a>
        <a class="btn btn-md btn-accent" href="https://www.youtube.com/watch?v=xvFZjo5PgG0">Quick fix</a>
    </div>
</div>

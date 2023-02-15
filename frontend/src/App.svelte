<script>
  import { onMount } from 'svelte';
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
  import {notes} from "./lib/store"
  import { Router, Route } from 'svelte-routing'
  import Home from "./lib/pages/Home.svelte"

  onMount(async () => {
		const res = await fetch(`http://ws:8000/`);
    const data = await res.json();
		notes.set(data);
	});
</script>


<h1 class="text-3xl font-bold underline">
 COSE DA FARE
</h1>

<Router>
  <Route component={Home} />
 
</Router>

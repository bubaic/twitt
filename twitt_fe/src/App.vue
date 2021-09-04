<template>
	<main>
		<TweetContainer />
	</main>
</template>

<script>
	import TweetContainer from "./components/tweet/TweetContainer";

	export default {
		components: { TweetContainer },
	};
</script>

<style lang="scss">
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}
	#app {
		font-family: 'liberian sans';
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		letter-spacing: 0.2vmin;
		color: #2c3e50;
		margin-top: 60px;
		// background: #ebebeb;

		main {
			max-width: 83.33%;
			margin: 5em auto;
			margin-bottom: 5em;
			margin-bottom: 10pt;
		}
	}
</style>

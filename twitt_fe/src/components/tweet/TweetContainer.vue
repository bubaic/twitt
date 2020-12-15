<template>
	<TweetForm />
	<TweetsList />
</template>

<script>
	import TweetsList from "./TweetsList";
	import TweetForm from "./TweetForm";
	import { provide } from "vue";

	export default {
		components: { TweetForm, TweetsList },
		setup: () => {
			const roles = ["like", "dislike", "retweet"];
			provide("roles", roles);
		},
	};
</script>

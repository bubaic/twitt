<template>
	<div id="tweets">
		<!-- <button @click="loadTweets">Load</button> -->
		<div v-if="isLoading">
			<Spinner />
		</div>
		<div v-else-if="hasTweets">
			<TweetItem
				v-for="t in tweets"
				:id="t.id"
				:key="t.id"
				:content="t.content"
				:likes="t.likes"
				:parent="t.parent"
				:rt="t.is_retweet"
			/>
		</div>
		<div v-else><h4>No tweets found!</h4></div>
	</div>
</template>

<script>
	import { mapGetters, mapActions } from "vuex";
	import TweetItem from "./TweetItem";
	import Spinner from "../layouts/SpinnerView";

	export default {
		components: { TweetItem, Spinner },
		data: function() {
			return { isLoading: false };
		},
		computed: {
			hasTweets: function() {
				return !this.isLoading && this.$store.getters["hasTweets"];
			},
			...mapGetters(["tweets"]),
		},
		methods: {
			loadTweets: async function() {
				this.isLoading = true;
				await this.$store.dispatch("setTweets");
				this.isLoading = false;
			},
		},
		created: function() {
			this.loadTweets();
		},
	};
</script>

<style lang="scss" scoped>
	@import "../../../../static/sass/_anime.scss";
	@import "../../../../static/sass/_mixins.scss";

	#tweets {
		display: grid;
		border-radius: 3pt;
		background: transparent;
		row-gap: 10pt;
		max-width: 75%;
		margin: auto;
		margin-top: 10pt;

		.tweet {
			@include delay(animation, 8, 0.2s);
			animation: slideInFade 600ms ease-out;
		}
	}
</style>

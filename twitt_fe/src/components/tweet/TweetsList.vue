<template>
	<div id="tweets">
		<div v-if="isLoading">
			<LoaderView />
			<LoaderView />
			<LoaderView />
		</div>
		<div v-else-if="hasTweets && !isLoading">
			<TweetItem
				v-for="t in tweets"
				:id="t.id"
				:key="t.id"
				:content="t.content"
				:likes="t.likes"
				:parent="t.parent"
				:rt="t.is_retweet"
				:timestamp="t.timestamp"
			/>
		</div>
		<div v-else><h4>No tweets found!</h4></div>
	</div>
</template>

<script>
	import { mapGetters } from "vuex";
	import TweetItem from "./TweetItem";
	import Spinner from "../layouts/SpinnerView";
	import LoaderView from "../layouts/LoaderView.vue";

	export default {
		components: { TweetItem, Spinner, LoaderView },
		data: function() {
			return { isLoading: false };
		},
		computed: {
			...mapGetters(["tweets", "hasTweets"]),
		},
		methods: {
			loadTweets: async function() {
				this.isLoading = true;
				try {
					await this.$store.dispatch("setTweets");
				} catch (e) {
					console.log(e || "Something went wrong!");
				}
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
		max-width: 83.33%;
		margin: auto;
		margin-top: 10pt;

		.tweet {
			// @include delay(animation, 8, 0.2s);
			animation: fadeIn 600ms ease-in-out;
		}
	}

	@media screen and (min-width: 320px) and (max-width: 420px) {
		#tweets {
			max-width: 250pt;
		}
	}
</style>

import { createStore } from "vuex";
import { lookup } from "../helper";

export default createStore({
	state: () => {
		return {
			tweets: [],
		};
	},
	getters: {
		tweets: (state) => {
			return state.tweets;
		},
		hasTweets: (state) => {
			return state.tweets && state.tweets.length > 0;
		},
		countLikes: (state) => {
			return state.tweets.likes;
		},
	},
	mutations: {
		loadTweets: (state, payload) => {
			state.tweets = payload;
		},
		addNewTweet: (state, payload) => {
			state.tweets.unshift(payload);
		},
	},
	actions: {
		createTweet: async (ctx, payload) => {
			const data = await lookup("POST", "tweets/create/", payload),
				newTweet = {
					id: data.id,
					content: data.content,
				};

			ctx.commit("addNewTweet", newTweet);
		},

		setTweets: async (ctx, payload) => {
			const data = await lookup("GET", "tweets/"),
				allTweets = [];

			for (const i in data) {
				const tweet = {
					id: data[i].id,
					content: data[i].content,
					likes: data[i].likes,
					is_retweet: data[i].is_retweet,
					parent: data[i].parent,
					timestamp: data[i].created,
				};
				allTweets.push(tweet);
			}

			ctx.commit("loadTweets", allTweets);
		},

		setAction: async (ctx, payload) => {
			const data = {
					id: payload.id,
					actions: payload.actions,
					content: payload.content,
				},
				response = await lookup("POST", "tweets/action/", data);

			console.log(response);
		},
	},

	// if any modules
	modules: {},
});

import { createStore } from "vuex";

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
	},
	mutations: {
		loadTweets: (state, payload) => {
			state.tweets = payload;
			// console.log(state.tweets.length);
		},
		addNewTweet: (state, payload) => {
			// const tweets = [...state.tweets];
			// tweets.unshift(payload);
			// state.tweets = tweets;

			state.tweets.unshift(payload);
			// console.log(state.tweets);
			// console.log(state.tweets.length);
		},
	},
	actions: {
		lookup: async (_, payload) => {
			const method = payload.method,
				url = payload.endpoint,
				body = payload.body;

			console.log("payload\n", payload);

			const response = await fetch(`http://localhost:8000/api/${url}`, {
					method: method,
					body: JSON.stringify(body),
				}),
				data = await response.json();

			if (!response.ok) {
				throw new Error(response.message || "Unable to fetch");
			}

			console.log("data from lookup", data);

			return data;
		},

		createTweet: async (ctx, payload) => {
			const newTweet = { content: payload.content },
				data = await ctx.dispatch("lookup", {
					endpoint: "tweets/create/",
					method: "POST",
					body: newTweet,
				});

			console.log("response data-->\n", data);

			ctx.commit("addNewTweet", newTweet);
		},

		setTweets: async (ctx, payload) => {
			const data = await ctx.dispatch("lookup", {
					endpoint: "tweets/",
					method: "GET",
				}),
				allTweets = [];

			for (const i in data) {
				const tweet = {
					id: data[i].id,
					content: data[i].content,
					likes: data[i].likes,
					is_retweet: data[i].is_retweet,
					parent: data[i].parent,
				};
				allTweets.push(tweet);
			}

			ctx.commit("loadTweets", allTweets);
		},
	},

	// if any modules
	modules: {},
});

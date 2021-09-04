<template>
	<span v-for="role in roles" :key="role">
		<button :role="role" :class="[role]" @click="handleActions(role)">
			<span v-if="role === 'like'">{{ likes }}</span>
			{{ role }}
		</button>
		<span>&nbsp;</span>
	</span>
</template>

<script>
	import { computed } from "vue";
	import { useStore } from "vuex";

	export default {
		props: ["roles", "likes", "tweetID", "tweetContent"],
		setup: (props) => {
			let likes = props.likes;
			const data = { id: props.tweetID },
				store = useStore();

			const actionData = (role) => {
				data["actions"] = role;

				if (role === "like") {
					likes += 1;
					console.log(likes);
				} else if (role === "dislike") {
					if (likes < 1) {
						likes = 0;
					} else {
						likes -= 1;
					}
					console.log(likes);
				} else if (role === "retweet") {
					console.log("it's a retweet");
					data["content"] = props.tweetContent;
				}

				return data;
			};

			function handleActions(role) {
				store.dispatch("setAction", actionData(role));
			}

			return { handleActions, likes };
		},
	};
</script>

<style lang="scss">
	button {
		max-width: 200pt;
		font-size: 10pt;
		text-transform: uppercase;
		word-wrap: break-word;
		background: #1c1e26;
		margin-right: auto;
		font-weight: 600;
		outline: 0;
		border: 0;
		padding: 4pt 8pt;
		color: #ebebeb;
		border-radius: 3pt;

		&:hover {
			background: #474c61;
		}
	}
	.like {
		background: #4169e1;

		&:hover {
			background: lighten(#4161e1, 10%);
		}
	}
	.dislike {
		background: #dc143c;

		&:hover {
			background: lighten(#dc1c3c, 10%);
		}
	}
	.retweet {
		background: #5f9f3f;

		&:hover {
			background: lighten(#5f9f3f, 10%);
		}
	}

	/* media query */
	@media screen and (min-width: 320px) and (max-width: 420px) {
		button {
			padding: 6pt;
			font-size: 8.5pt;
		}
	}

	// if liked
	.liked {
		background: red;
	}
	.notliked {
		background: transparent;
	}
</style>

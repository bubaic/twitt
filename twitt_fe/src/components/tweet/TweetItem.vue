<template>
	<div class="tweet" :id="'tweet-' + id">
		<h6>timestamp</h6>
		<p>{{ content }}</p>
		<ButtonView :roles="roles" :likes="likes" @handle-action="handleActions" />
	</div>
</template>

<script>
	import { computed, inject } from "vue";
	import ButtonView from "../layouts/ButtonView";

	export default {
		components: { ButtonView },
		props: ["id", "content", "likes", "rt", "parent"],

		setup: (props) => {
			const roles = inject('roles'),
				url = "/api/tweets/action",
				method = "POST",
				likes = props.likes,
				data = { id: props.id };

			function handleActions(role) {
				if (role === "like") {
					data["actions"] = role;
					// console.log(JSON.stringify(data), props.id, props.likes, );
				} else if (role === "dislike") {
					data["actions"] = role;
					console.log(data);
				} else if (role === "retweet") {
					data["actions"] = role;
					console.log(data);
				}
			}

			return { roles, handleActions, likes };
		},
	};
</script>

<style lang="scss" scoped>
	.tweet {
		// border: 1pt solid #e1e1e1;
		box-shadow: 0 0pt 4pt #50505040;
		background: #ebebeb;
		padding: 15pt 20pt;
		text-align: start;
		margin-bottom: 10pt;

		p,
		h6 {
			font-family: "alegreya sans";
		}

		p {
			margin-bottom: 10pt;
		}

		h6 {
			float: right;
		}
	}
</style>

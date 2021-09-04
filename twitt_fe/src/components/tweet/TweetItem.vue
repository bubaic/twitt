<template>
	<div class="tweet" :id="'tweet-' + id">
		<div class="time-n-action">
			<small v-if="rt">RT</small>
			<sub>&nbsp;{{ id }}, {{ parent }}</sub>
			<h6>{{ creationTime }}</h6>
			<span class="more" role="button" @click="toggleMoreOpts"></span>
			<div class="more-opts">
				<span>delete</span>
			</div>
		</div>
		<p>{{ content }}</p>
		<ButtonView
			:roles="roles"
			:likes="likes"
			:tweetID="id"
			:tweetContent="content"
		/>
	</div>
</template>

<script>
	import { inject } from "vue";
	import { mapGetters, useStore } from "vuex";
	import ButtonView from "../layouts/ButtonView";

	export default {
		components: { ButtonView },
		props: ["id", "content", "likes", "rt", "parent", "timestamp"],
		setup: (props) => {
			const id = props.id,
				likes = props.likes,
				date = new Date(props.timestamp),
				content = props.content,
				rt = props.rt,
				roles = inject("roles");

			const creationTime =
				date.toDateString().substr(8, 2) +
				" " +
				date.toDateString().substr(4, 3) +
				", " +
				date.toDateString().substr(11, 4);

			function handleRetweet() {}

			return { id, likes, roles, creationTime, content, rt };
		},
	};
</script>

<style lang="scss" scoped>
	.tweet {
		border: 1pt solid #e1e1e1;
		border-radius: 4pt;
		// box-shadow: 0 1pt 2pt #50505040;
		padding: 15pt 20pt;
		text-align: start;
		margin-bottom: 10pt;

		&:last-child {
			border: none;
		}

		p,
		h6 {
			font-family: sans-serif;
		}

		p {
			margin-bottom: 10pt;
		}

		.time-n-action {
			// float: right;
			display: flex;
			align-items: center;
			justify-content: space-between;
			position: relative;
			top: -6pt;

			h6 {
				font-size: 7pt;
				cursor: default;
				padding-right: 8pt;
				font-weight: bold;
				margin-left: auto;
			}
			small {
				color: rgb(18, 187, 18);
				text-shadow: 0 0 2pt rgba(0, 0, 0, 0.25);
				font-weight: bolder;
				position: relative;
				top: -1pt;
			}

			.more {
				left: 6pt;
				top: -1pt;
				height: 5pt;
				width: 5pt;
				display: block;
				border-radius: 50%;
				position: relative;
				background: #9e9e9e;

				&::before {
					position: absolute;
					display: block;
					content: "";
					left: -7pt;
					width: 5pt;
					height: 5pt;
					border-radius: 50%;
					background: inherit;
				}

				&::after {
					position: absolute;
					display: block;
					content: "";
					left: 7pt;
					width: 5pt;
					height: 5pt;
					border-radius: 50%;
					background: inherit;
				}
			}

			.more-opts {
				display: none;
			}
		}
	}
</style>

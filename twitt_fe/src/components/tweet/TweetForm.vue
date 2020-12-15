<template>
	<div id="create">
		<form @submit.prevent="submitData" class="form">
			<!-- {% csrf_token %} -->
			<div id="tweet-errors"></div>
			<input name="next" type="hidden" value="/" />
			<textarea
				class="form-control"
				name="content"
				placeholder="what's in your mind"
				required
				rows="6"
				v-model.trim="content"
			/>
			<button>Tweet</button>
		</form>
	</div>
</template>

<script>
	export default {
		data: function() {
			return { content: "" };
		},
		methods: {
			submitData: function() {
				this.$store.dispatch("createTweet", { content: this.content });
				this.content = "";
			},
		},
	};
</script>

<style lang="scss">
	#create {
		margin-bottom: 10pt;
		border: 1pt solid #e0e0e0;
		background: #f5f5f5;
		display: grid;
		border-radius: 3pt;
		row-gap: 10pt;
		max-width: 75%;
		margin: auto;

		textarea {
			width: 100%;
			border: 0;
			outline: 0;
			padding: 10pt;
			resize: none;
		}

		button {
			float: right;
			margin: 8pt;
			background: #1c1e26;
		}
	}
</style>

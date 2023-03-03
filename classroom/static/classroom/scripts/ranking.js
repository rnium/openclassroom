function get_ranking_data() {
    $.ajax({
        type: "get",
        url: ranking_api_url,
        dataType: "json",
        cache: false,
        success: function(response) {
            console.log(response);
        },
        error: function(error, xhr, status) {
            console.log(error);
        },
    });
}

get_ranking_data()



{/* <div class="container">
				<div class="row">
					<div class="col-sm-4 second" style="display: none;">
						<div class="leaderboard-card">
							<div class="leaderboard-card__top">
								<h3 class="text-center">1,051</h3>
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="img/user2.jpg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0">Sandeep Sandy</h5>
									<p class="text-muted mb-0">2018338514</p>
									<img src="./img/second-rank.png" alt="" class="rank-icon my-3">
									
									<hr>
									<!-- <div class="lb-action d-flex justify-content-between align-items-center">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Second Rank</span></span>
										<button class="btn btn-outline-success btn-sm">Congratulate</button>
									</div> -->
									<div class="stats d-flex justify-content-around align-items-center my-2">
										<div class="s-item">
											<span class="label">Participation:</span>
											<span class="value">85%</span>
										</div>
										<div class="s-item">
											<span class="label">Regularity:</span>
											<span class="value">367</span>
										</div>
									</div>
									<hr>
									<div class="lb-action d-flex justify-content-center align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Second Rank</span></span>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-4 second empty">
						<div class="leaderboard-card">
							<div class="leaderboard-card__top pt-5 pb-3">
								
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="../images/blank-dp.svg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0"></h5>
									<p class="text-muted mb-0"></p>
									<img src="./img/medals.png" alt="" class="rank-icon my-3">
									
									<hr>
									<!-- <div class="lb-action d-flex justify-content-between align-items-center">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Second Rank</span></span>
										<button class="btn btn-outline-success btn-sm">Congratulate</button>
									</div> -->
									<div class="info text-muted my-2">Excellence to be achieved</div>
									<hr>
									<div class="lb-action d-flex justify-content-center align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Reserved Second Rank</span></span>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-4 first" style="display: none;">
						<div class="leaderboard-card leaderboard-card--first">
							<div class="leaderboard-card__top">
								<h3 class="text-center">1,254</h3>
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="img/user1.jpg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0">Kiran Acharya</h5>
									<p class="text-muted mb-0">@kiranacharyaa</p>
									<img src="./img/first_rank.png" alt="" class="rank-icon my-3">
									<hr>
									<div class="stats d-flex justify-content-around align-items-center my-2">
										<div class="s-item">
											<span class="label">Participation:</span>
											<span class="value">85%</span>
										</div>
										<div class="s-item">
											<span class="label">Regularity:</span>
											<span class="value">367</span>
										</div>
									</div>
									<hr>
									<div class="lb-action d-flex justify-content-between align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">First Rank</span></span>
										<button class="btn btn-outline-success btn-sm">Congratulate</button>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-4 first empty">
						<div class="leaderboard-card leaderboard-card--first">
							<div class="leaderboard-card__top pt-5">
								
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="../images/blank-dp.svg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0"></h5>
									<p class="text-muted mb-0"></p>
									<img src="./img/trophy.png" alt="" class="rank-icon my-3">
									<hr>
									<div class="info text-muted my-2">Excellence to be achieved</div>
									<hr>
									<div class="lb-action d-flex justify-content-center align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Reserved First Rank</span></span>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-4 third" style="display: none;">
						<div class="leaderboard-card">
							<div class="leaderboard-card__top">
								<h3 class="text-center">1,012</h3>
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="img/user3.jpg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0">John doe</h5>
									<p class="text-muted mb-0">@johndoe</p>
									<img src="./img/third-rank.png" alt="" class="rank-icon my-3">
									<hr>
									<div class="stats d-flex justify-content-around align-items-center my-2">
										<div class="s-item">
											<span class="label">Participation:</span>
											<span class="value">95%</span>
										</div>
										<div class="s-item">
											<span class="label">Regularity:</span>
											<span class="value">564</span>
										</div>
									</div>
									<hr>
									<div class="lb-action d-flex justify-content-between align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Third Rank</span></span>
										<button class="btn btn-outline-success btn-sm">Congratulate</button>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-sm-4 third empty">
						<div class="leaderboard-card">
							<div class="leaderboard-card__top pt-5 pb-3">
								
							</div>
							<div class="leaderboard-card__body">
								<div class="text-center">
									<img src="../images/blank-dp.svg" class="circle-img mb-2" alt="User Img">
									<h5 class="mb-0"></h5>
									<p class="text-muted mb-0"></p>
									<img src="./img/medals.png" alt="" class="rank-icon my-3">
									
									<hr>
									<!-- <div class="lb-action d-flex justify-content-between align-items-center">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Second Rank</span></span>
										<button class="btn btn-outline-success btn-sm">Congratulate</button>
									</div> -->
									<div class="info text-muted my-2">Excellence to be achieved</div>
									<hr>
									<div class="lb-action d-flex justify-content-center align-items-center mt-2">
										<span class="leaderboard-info"><img class="lb-icon" src="./img/leaderboard.svg" alt=""><span class="txt">Reserved Third Rank</span></span>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
	
				<table class="table">
					<thead>
						<tr>
							<th>Student</th>
							<th>Points</th>
							<th>Participation</th>
							<th>Regularity</th>
							<th>Rank</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>
								<div class="d-flex align-items-center">
									<img src="img/user1.jpg" class="circle-img circle-img--small mr-2" alt="User Img">
									<div class="user-info__basic">
										<h5 class="mb-0">Kiran Acharya</h5>
										<p class="text-muted mb-0">2014338514</p>
									</div>
								</div>
							</td>
							<td>
								<div class="d-flex align-items-baseline">
									<h4 class="mr-1">1,253</h4>
								</div>
							</td>
							<td>78%</td>
							<td>4546</td>
							<td>4</td>
						</tr>
						<tr class="unranked">
							<td>
								<div class="d-flex align-items-center">
									<img src="img/user2.jpg" class="circle-img circle-img--small mr-2" alt="User Img">
									<div class="user-info__basic">
										<h5 class="mb-0">Kiran Acharya</h5>
										<p class="text-muted mb-0">2014338514</p>
									</div>
								</div>
							</td>
							<td>
								<div class="d-flex align-items-baseline">
									<h4 class="mr-1">1,253</h4>
								</div>
							</td>
							<td>78%</td>
							<td>4546</td>
							<td>--</td>
						</tr>
						
					</tbody>
				</table>
			</div> */}
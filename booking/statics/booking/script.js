// const user_id = $("meta[name=user_id]").attr("content")

$.ajax({
  url: "/booking/get",
  // url: "/booking/get/${user_id}",
  type: "GET",
  beforeSend: () => { 
    let html = "";
    html += `
    <div class="card" style="width: 48rem;">
      <div class="card-body container-dim">
        <h5>Loading</h5>
      </div>
    </div>
    `;

    $("#booking").html(html);
  },
}).done((data) => {
    let html = "";
    // data = list of todo

    for (let i = 0; i < data.length; i++) {
        html += `
        <table>
            <tr>
                <th style="background-color: #C6F37C;">ID</th>
                <th style="background-color: #C6F37C;">Lokasi</th>
                <th style="background-color: #C6F37C;">Check-in</th>
                <th style="background-color: #C6F37C;">Check-out</th>
                <th style="background-color: #C6F37C;">Status</th>
            </tr>
            {% for note in notes %}
            <tr>
                <td>${data[i].fields.ID_booking}</td>
                <td>${data[i].fields.ID_rental}</td>
                <td>${data[i].fields.tanggal_checkin}</td>
                <td>${data[i].fields.tanggal_checkout}</td>
                <td>Menunggu Pembayaran</td>
            </tr>
            {% endfor %}
        </table>
        `; 
      }
      
      $("#booking").html(html);
});

{/* <div class="wadah-card">
        <div class="card" style="width:18rem;">
          <div class="card-header">
            ${data[i].fields.matkul}
          </div>
          <div class="card-body">
            <h5 class="card-title">${data[i].fields.judul}</h5>
            <h5 class="card-text mb-2" style="color:red;">${data[i].fields.tanggal} ${data[i].fields.waktu}</h5>
            <p class="card-text">${data[i].fields.keterangan}</p>
            <a href="/agenda/delete/${data[i].pk}" class="btn btn-danger bottom">Hapus</a>
          </div>
        </div>
        </div> */}
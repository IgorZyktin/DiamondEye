% rebase('base.tpl')
% if image_url:
<div class="main_container">
    <div class="main_image">
        <img class="" src="{{ image_url }}" alt=""/>
    </div>
    <div id="main_description" class="main_description">
        <a class="btn active" onclick="confirmChanges()">Confirm changes</a>
        <a class="btn active" onclick="addTag('main_description')">Add tag</a>
    </div>
</div>
% else:
<p>No image with id <strong>{{ uuid }}</strong> has been found.</p>
% end
<br>
<br>

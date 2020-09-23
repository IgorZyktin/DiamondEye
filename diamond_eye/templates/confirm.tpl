% rebase('base.tpl')
<div class="confirm">
    <div class="unconfirmed_image">
        <h2>Total images: {{ len(images) }}</h2>
        <a href="#" class="btn active w-100" onclick="addTagBatch()">Add
            tag</a>
    </div>
    % for i, image in enumerate(images):
    <div class="unconfirmed_image {{ 'duplicate_div' if image.duplicate else '' }}">
        <div class="f_row">
            <div class="strict">
                <img class="new_image" src="{{ image.url }}"
                     alt="{{ image.filename }}"/>
            </div>
            <div class="f_col">
                <div id="div_{{ i }}">
                    % if image.duplicate:
                    <h3>Already exist:</h3>
                    <img class="duplicate_image"
                         src="{{ image.duplicate }}"
                         alt=""/>
                    % else:
                    <a class="btn active"
                       onclick="addTag('div_{{ i }}')">Add tag</a>
                    % end
                </div>
            </div>
        </div>
    </div>
    % end
    <a class="btn active big_btn w-100" onclick="confirmAll()">Confirm
        all</a>
    <a class="btn active big_btn w-100" onclick="dropAll()">Drop
        all</a>
    <br>
    <br>
</div>
